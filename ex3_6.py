#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    input_data=input()
    '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: tuple
    '''
    assert (input_data in range(1, 13)), "Tháng không tồn tại"
    result = ("MONTH", "DATE")

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    for i in range(13):
        if i == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            print (month,31)
        elif i == 2 :
            print(month,28)
        else:
            print (month,30)
        month, day = solve(2)
        print(month, day)


if __name__ == "__main__":
    main()
