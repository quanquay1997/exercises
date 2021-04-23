#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve(year,name):
    can = ('giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý')
    chi = ('tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
           'tuất', 'hợi')
    year = int(input("nhap nam can xem:"))
    vitri_can = year % 10
    vitri_chi = year % 12
    name = can[vitri_can] + " " + chi[vitri_chi]
    print(can[vitri_can] + " " + chi[vitri_chi])



    '''Trả về tuple-2 chứa year và tên gọi can chi tương ứng. Các từ trong tên
    đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Năm 2017 là năm "Đinh Dậu".
    '''

    # result = None
    #
    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result

def main():
    print("Năm {0} là năm {1}".format(*solve(1696)))
#
# if __name__ == "__main__":
#     main()
