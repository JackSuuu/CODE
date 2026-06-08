import argparse
import numpy as np
import cv2
import sys

def compute_energy(img):
    """
    Compute the energy map of an image using the gradient magnitude (Sobel).
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    energy = np.abs(sobel_x) + np.abs(sobel_y)
    return energy

def find_vertical_seam(energy):
    """
    Find the vertical seam of least energy using dynamic programming.
    Returns a list of (row, col) indices from top to bottom.
    """
    h, w = energy.shape
    dp = energy.copy()
    backtrack = np.zeros_like(dp, dtype=np.int32)

    # Build DP table
    for i in range(1, h):
        for j in range(w):
            # Look at three possible pixels above (clamped to image boundaries)
            left = dp[i-1, j-1] if j-1 >= 0 else np.inf
            up   = dp[i-1, j]
            right= dp[i-1, j+1] if j+1 < w else np.inf

            # Pick the minimum
            idx_min = np.argmin([left, up, right])
            dp[i, j] += [left, up, right][idx_min]

            # Store backtrack (column index of chosen predecessor)
            if idx_min == 0:
                backtrack[i, j] = j-1
            elif idx_min == 1:
                backtrack[i, j] = j
            else:
                backtrack[i, j] = j+1

    # Retrace seam from bottom row
    seam = []
    j = int(np.argmin(dp[-1]))
    for i in range(h-1, -1, -1):
        seam.append((i, j))
        j = backtrack[i, j]
    seam.reverse()
    return seam

def remove_vertical_seam(img, seam):
    """
    Remove the given vertical seam from the image.
    """
    h, w, _ = img.shape
    mask = np.ones((h, w), dtype=np.bool_)
    for i, j in seam:
        mask[i, j] = False
    # Use the mask to compress each row
    output = img[mask].reshape((h, w-1, 3))
    return output

def carve_seams(img, num_seams):
    """
    Iteratively remove 'num_seams' vertical seams.
    """
    carved = img.copy()
    for k in range(num_seams):
        energy = compute_energy(carved)
        seam = find_vertical_seam(energy)
        carved = remove_vertical_seam(carved, seam)
        if (k+1) % 10 == 0 or k == num_seams-1:
            print(f"Removed {k+1}/{num_seams} seams; new size = {carved.shape[1]}×{carved.shape[0]}")
    return carved

def main():
    parser = argparse.ArgumentParser(description="Seam Carving (vertical) with Dynamic Programming")
    parser.add_argument("--input",  "-i", required=True, help="Path to input image")
    parser.add_argument("--output", "-o", required=True, help="Path to save the carved image")
    parser.add_argument("--seams",  "-s", type=int, default=50, help="Number of vertical seams to remove")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        print(f"Error: Could not read image '{args.input}'", file=sys.stderr)
        sys.exit(1)

    carved = carve_seams(img, args.seams)
    cv2.imwrite(args.output, carved)
    print(f"Done! Saved carved image to '{args.output}'")

if __name__ == "__main__":
    main()
