#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    # result = None
    #
    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    # return result


def main():
    # Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
    numbers = range(-10, 11)
    numbers = list(numbers)
    numbers.remove(0)
    tong = 0
    tich = 1
    for i in numbers:
        tong = tong+i
        # tong.append(i)
    print(tong)
    for j in numbers:
        tich = tich * j
        # tich.append(j)
    print(tich)

