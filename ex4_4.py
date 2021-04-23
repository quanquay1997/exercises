#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import time


def solve():
    '''Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66

    Bài toán lớp 3 có số đáp án khổng lồ
    (http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)
    '''

    # result = None
    #
    # # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result


def main():
    time
    len([(a, b, c, d, e, f, g, h, i) for a in range(1, 10) for b in range(1, 10) for c in range(1, 10) for d in
         range(1, 10) for e in range(1, 10) for f in range(1, 10) for g in range(1, 10) for h in range(1, 10) for i in
         range(1, 10) if a + 13 * b / c + d + 12 * e - f + g * h / i == 66])
    for i in len():
        print i
#
# if __name__ == "__main__":
#     main()
