#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
data = ('Able was I ere I saw Elba')
ans = solve(data)
if (ans):
    print ("Yes")
else:
    print ("No")


    '''Kiểm tra text có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 1 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result


def main():
    print(solve('Able was I ere I saw Elba'))


if __name__ == "__main__":
    main()
