#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import string
# words = string.ascii_lowercase
# def solve(words):
#     for i in words(0-25):
#         words[i] = +1

    #
    # '''Trả về list chứa điểm tương ứng của các từ trong `words`
    #
    # Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    # thì từ ``attitude`` có giá trị bằng 100.
    # (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)
    #
    # Gợi ý::
    #
    #   import string
    #   print(string.ascii_lowercase)
    # '''

    # result = None
    #
    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result

#
# def main():
#     words = ['numpy', 'django', 'saltstack', 'discipline',
#              'Python', 'FAMILUG', 'pymi']
#
#     print(solve(words))
#
#
# if __name__ == "__main__":
#     main()
def sum(chuoi):
    chuoi = chuoi.lower()
    tong = 0
    for kytu in chuoi:
        gt = ord(kytu) - 96
        tong += gt
    return tong
def main():
    words = ['numpy', 'django', 'saltstack', 'discipline',
            'Python', 'FAMILUG', 'pymi']
    for chuoi in words:
        print chuoi, sum(chuoi)
    main()