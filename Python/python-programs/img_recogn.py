import cv2
import os

# Initialize the face recognizer
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    return img, faces

# Function to draw rectangles around detected faces
def draw_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return image

# Main function to process an image
def process_image(image_path):
    image, faces = detect_faces(image_path)
    image_with_faces = draw_faces(image, faces)

    cv2.imshow('Faces found', image_with_faces)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'  # Replace with your image path
    process_image(image_path)