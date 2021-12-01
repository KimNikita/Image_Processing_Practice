import sys
import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import glob


def DFFTnp(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    return fshift


def reverseDFFTnp(dfft):
    f_ishift = np.fft.ifftshift(dfft)
    reverse_image = np.fft.ifft2(f_ishift)
    return reverse_image


folder_path = os.path.abspath("") + 'stripes/'
images = glob.glob(folder_path + '*.png')
for image in images:
    img = np.float32(cv.imread(image, 0))
    fshift = DFFTnp(img)

    plt.subplot(121), plt.title('Input spectrum')
    plt.imshow(np.abs(fshift), norm=LogNorm(vmin=5))

    w, h = fshift.shape
    maxpix = fshift[w//2][h//2]
    for i in range(w):
        for j in range(h):
            if i != w//2 and j != h//2:
                if abs(np.abs(fshift[i][j])-np.abs(maxpix)) < np.abs(maxpix) - 270000:
                    fshift[i][j] = 0

    plt.subplot(122), plt.title('Custom Notch filter')
    plt.imshow(np.abs(fshift), norm=LogNorm(vmin=5))
    plt.show()

    reverse_image = reverseDFFTnp(fshift)

    plt.subplot(121), plt.title('Input image')
    plt.imshow(abs(img), cmap='gray')
    plt.subplot(122), plt.title('Result image')
    plt.imshow(abs(reverse_image), cmap='gray')
    plt.show()
