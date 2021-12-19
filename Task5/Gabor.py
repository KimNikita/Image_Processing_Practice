# -*- coding: utf-8 -*-
"""
@author: Kim Nikita
"""

import os
import cv2 as cv
import numpy as np
from skimage.io import imread


def RGB2GRAY(img):
    # Grayscale
    gray = 0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2]
    return gray


def Gabor_filter(K_size=11, Sigma=1.5, Gamma=1.2, Lambda=3, Psi=0, angle=0):
    # get half size
    d = K_size // 2

    # prepare kernel
    gabor = np.zeros((K_size, K_size), dtype=np.float32)

    # each value
    for y in range(K_size):
        for x in range(K_size):
            # distance from center
            px = x - d
            py = y - d

            # degree -> radian
            theta = angle / 180. * np.pi

            # get kernel x
            _x = np.cos(theta) * px + np.sin(theta) * py

            # get kernel y
            _y = -np.sin(theta) * px + np.cos(theta) * py

            # fill kernel
            gabor[y, x] = np.exp(-(_x**2 + Gamma**2 * _y**2) /
                                 (2 * Sigma**2)) * np.cos(2*np.pi*_x/Lambda + Psi)

    # kernel normalization
    gabor /= np.sum(np.abs(gabor))

    return gabor


def Gabor_filtering(gray, K_size=11, Sigma=1.5, Gamma=1.2, Lambda=3, Psi=0, angle=0):
    # get shape
    H, W = gray.shape

    # padding
    # gray = np.pad(gray, (K_size//2, K_size//2), 'edge')

    # prepare out image
    out = np.zeros((H, W), dtype=np.float32)

    # get gabor filter
    gabor = Gabor_filter(K_size=K_size, Sigma=Sigma,
                         Gamma=Gamma, Lambda=Lambda, Psi=0, angle=angle)

    # filtering

    out = cv.filter2D(gray, -1, gabor)

    out = np.clip(out, 0, 255)
    out = out.astype(np.uint8)

    return out


def Gabor_process(img):
    # get shape
    H, W, _ = img.shape

    # gray scale
    gray = RGB2GRAY(img).astype(np.float32)

    # define angle
    As = [0, 30, 60, 90, 120, 150]

    out = np.zeros([H, W], dtype=np.float32)

    # each angle
    for i, A in enumerate(As):
        # gabor filtering
        _out = Gabor_filtering(gray, K_size=11, Sigma=1.5,
                               Gamma=1.2, Lambda=3, angle=A)

        # add gabor filtered image
        out += _out

    # scale normalization
    out = out / out.max() * 255
    out = out.astype(np.uint8)

    return out


# Read images
inputs = []
results = []
fingers = os.path.abspath('') + '/fingers/'
i = 0
for finger in os.listdir(fingers):
    i += 1
    # i hate cv.imread, this *** not *** working for me sometimes
    img = imread(fingers+finger).astype(np.float32)
    inputs.append(cv.resize(imread(fingers+finger), (0, 0), fx=1.5, fy=1.5))
    # gabor process
    out = Gabor_process(img)
    results.append(cv.resize(out, (0, 0), fx=1.5, fy=1.5))

for i in range(len(inputs)):
    cv.imshow("Finger input {}".format(i+1), inputs[i])
    cv.imshow("Finger output {}".format(i+1), results[i])
    cv.waitKey(0)
    cv.destroyAllWindows()
