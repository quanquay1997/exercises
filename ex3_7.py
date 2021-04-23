#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
'''


def solve():
    j=[]
    stt = 0
    for i in range(0,101):
        if i % 5 == 0:
                j.append("%s = %s * 5"%(i,i%5))
    print j


    '''Trả về 1 `list` các `string` có dạng:

        output: ['5 == 1 * 5', '10 == 2 * 5', ...]

    Lưu ý: Thứ tự tăng dần theo bảng cửu chương
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    for i in solve(101):
        if i % 5 == 0 or 5:
            print(i)


if __name__ == "__main__":
    main()
