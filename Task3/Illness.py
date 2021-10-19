import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt


def SegmentIllness(images, filter=0):
    markers = []
    marker1 = np.zeros((256, 256), dtype="int32")  # болезнь
    marker1[75: 200, 75: 140] = 255  # лист
    marker1[0: 55, 0: 20] = 1  # лево верх
    marker1[0: 145, 180: 255] = 1  # лево низ
    marker1[170: 255, 0: 15] = 1  # право верх
    marker1[175: 255, 175: 255] = 1  # право низ
    markers.append(marker1)

    marker2 = np.zeros((256, 256), dtype="int32")
    marker2[100: 160, 140: 175] = 255
    marker2[0: 45, 0: 40] = 1
    marker2[0: 60, 190: 255] = 1
    marker2[200: 255, 0: 45] = 1
    marker2[180: 255, 175: 255] = 1
    markers.append(marker2)

    marker3 = np.zeros((256, 256), dtype="int32")
    marker3[80: 160, 55: 110] = 255
    marker3[0: 40, 0: 30] = 1
    marker3[0: 150, 180: 255] = 1
    marker3[205: 255, 0: 35] = 1
    marker3[220: 255, 145: 255] = 1
    markers.append(marker3)

    marker4 = np.zeros((256, 256), dtype="int32")
    marker4[105: 210, 55: 140] = 255
    marker4[0: 40, 0: 60] = 1
    marker4[0: 45, 180: 255] = 1
    marker4[230: 255, 0: 105] = 1
    marker4[170: 255, 195: 255] = 1
    markers.append(marker4)

    marker5 = np.zeros((256, 256), dtype="int32")
    marker5[120: 190, 110: 190] = 255
    marker5[0: 50, 0: 40] = 1
    marker5[0: 60, 205: 255] = 1
    marker5[220: 255, 0: 60] = 1
    marker5[210: 255, 215: 255] = 1
    markers.append(marker5)

    results = []
    for i, image in enumerate(images):
        if filter == 0:
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
            image = cv.erode(image, kernel)
        elif filter == 1:
            # src, kernel, sigmaColor, sigmaSpace
            image = cv.bilateralFilter(image, 3, 100, 100)
        else:
            # src, dst, сила размытия, 10, 7, 21
            image = cv.fastNlMeansDenoisingColored(image, None, 100, 10, 7, 21)

        hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        leafs_area_BGR = cv.watershed(image, markers[i])

        # я дальтоник, так что поверю что тут правильные границы цвета
        healthypart = cv.inRange(hsv_img, (36, 25, 25), (86, 255, 255))
        ill_part = leafs_area_BGR - healthypart
        mask = np.zeros_like(image, np.uint8)
        mask[leafs_area_BGR > 1] = (255, 0, 255)
        mask[ill_part > 1] = (0, 0, 255)
        results.append(mask)
    return results


path = os.path.abspath('') + '/test/'
inputt = []

for image in os.listdir(path):
    inputt.append(cv.imread(path+image))

# 0 || 1 || 2
output = SegmentIllness(inputt, 0)

for i in range(5):
    fig, (a, b) = plt.subplots(1, 2, figsize=(12, 8))
    a.imshow(inputt[i])
    b.imshow(output[i])
    plt.show()
