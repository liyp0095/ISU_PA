#!/bin/python
# -*- coding: utf8 -*-

'''
Description: This is for the test of 2d FFT
Auther: Yuepei Li
Date: 2019-12-12
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

def read_img():
    img = cv2.imread("sample.jpg", 0)
    print(img)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def fft2(img):
    f_img = np.fft.fft2(img)
    f_img = np.fft.fftshift(f_img)
    return f_img


def ifft2(f_img):
    f_ishift = np.fft.ifftshift(f_img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back


def main():
    img = read_img()
    f_img = fft2(img)

    plt.subplot(221),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(20*np.log(np.abs(f_img)), cmap = 'gray')
    plt.title('FFT Output'), plt.xticks([]), plt.yticks([])

    rows, cols = img.shape
    crow, ccol = int(rows/2) , int(cols/2)

    # mask is for high pass
    mask = np.zeros((rows,cols), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 1

    f_img_copy1 = f_img.copy()
    f_img_copy2 = f_img.copy()
    f_img_copy1[crow-30:crow+30, ccol-30:ccol+30] = 0
    f_img_copy2 = f_img_copy2 * mask
    img_back1 = ifft2(f_img_copy1)
    img_back2 = ifft2(f_img_copy2)

    plt.subplot(223),plt.imshow(img_back2, cmap = 'gray')
    plt.title('Low Pass Filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(img_back1, cmap = 'gray')
    plt.title('High Pass Filter'), plt.xticks([]), plt.yticks([])

    plt.show()
    pass


if __name__ == "__main__":
    main()
