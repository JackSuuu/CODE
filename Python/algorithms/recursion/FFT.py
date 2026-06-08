import numpy as np

# 快速傅立叶变换 - Fast Fourier Transform
def fft_recursive(x):
    N = x.shape[0]

    if N <= 1:
        return x

    even = fft_recursive(x[::2])
    odd = fft_recursive(x[1::2])

    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even + factor[:N // 2] * odd,
                           even + factor[N // 2:] * odd])


def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("Input array size must be a power of 2")

    return fft_recursive(x)


if __name__ == "__main__":
    x = np.random.random(1024)
    np.testing.assert_allclose(fft(x), np.fft.fft(x), rtol=1e-6, atol=1e-6)
    print("The custom FFT implementation is correct.")
