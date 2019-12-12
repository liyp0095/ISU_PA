#!/bin/python
# -*- coding: utf8 -*-

'''
Description: This file is used for test the function in ...
Auther: Yuepei Li
Date: 2019-12-10
'''

from math import cos, sin, pi
import matplotlib.pyplot as plot
import numpy as np

from fft import  DFT, IDFT


def sig1(x):
    # return cos(x)+cos(50*x)+cos(100*x)
    return cos(x)+cos(10*x)+cos(50*x)+cos(100*x)+cos(500*x)+cos(1000*x)


def sig2(x):
    return 4*np.exp(-0.6*x) * np.sin(1/8*np.pi*x)


def sig3(x):
    return 0.15*cos(200*x) + 0.65*cos(300*x) + 0.4*cos(77*x) + 0.6*cos(70*x)


def lowpass_filter(length, x):
    f = [0] * length
    for i in range(x):
        f[i] = 1
        f[-(i+1)] = 1
    return f


def time_line(start, end, interval):
    N = int((end - start) / interval)
    return [start + i*interval for i in range(N)]


def signal_extraction():
    print("================ signal extraction =================")
    time = time_line(0, 10, 0.01)
    a = [sig1(i) for i in time]
    b = DFT(a)

    plot.figure()
    fg = plot.subplot(131)
    fg.plot(time, a)
    fg.set_title("(a) Time Domain")

    fg = plot.subplot(133)
    fp = plot.plot([i/10*2*pi for i in time], [abs(i)/len(b) for i in b])
    fg.set_title("(c) Frequency Domain")

    fg = plot.subplot(632)
    fg.plot(time, [cos(x) for x in time])
    fg.set_title("(b) Frequency Component")
    fg = plot.subplot(635)
    fg.plot(time, [cos(10*x) for x in time])
    fg = plot.subplot(638)
    fg.plot(time, [cos(50*x) for x in time])
    fg = plot.subplot(6,3,11)
    fg.plot(time, [cos(100*x) for x in time])
    fg = plot.subplot(6,3,14)
    fg.plot(time, [cos(500*x) for x in time])
    fg = plot.subplot(6,3,17)
    fg.plot(time, [cos(1000*x) for x in time])
    plot.show()


def filter_example():
    print("================ signal extraction =================")
    time = time_line(0, 10, 0.01)
    signal = [sig2(i) for i in time]
    noise = [sig3(i) for i in time]
    sig_with_noi = [signal[i] + noise[i] for i in range(len(signal))]

    # print(np.fft.ifft(np.fft.fft(signal)))

    plot.figure()
    fg = plot.subplot(231)
    fg.plot(time, signal)
    fg.set_title("(a) Signal")
    fg = plot.subplot(232)
    fg.plot(time, noise)
    fg.set_title("(b) Noise")
    fg = plot.subplot(233)
    fg.plot(time, sig_with_noi)
    fg.set_title("(c) Signal with Noise")
    # plot.show()

    f_sig = np.fft.fft(sig_with_noi)
    # print(f_sig)
    filter = lowpass_filter(len(f_sig), 20)
    f_sig_filter = [filter[i]*f_sig[i] for i in range(len(filter))]
    sig = np.fft.ifft(f_sig_filter)
    # f_sig =
    # plot.figure()
    fg = plot.subplot(234)
    fg.plot(time, [abs(i)/len(time) for i in f_sig])
    fg.plot(time, lowpass_filter(len(time), 30))
    fg.set_title("(d) Frequency Domain")
    fg = plot.subplot(235)
    fg.plot(time, [abs(i)/len(time) for i in f_sig_filter])
    fg.set_title("(e) Frequency After Filter")
    plot.ylim((0, 1))
    fg = plot.subplot(236)
    fg.plot(time, sig)
    fg.set_title("(f) Signal After Filter")
    plot.show()


def main():
    signal_extraction()
    pass





if __name__ == "__main__":
    main()
