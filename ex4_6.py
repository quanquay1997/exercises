#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve(text):
    text= "Bé lên 3 bé đi lớp 4"
    [int (i) for i in text.split() if i.isdigit()]


    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    '''

    result = None

    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result

#
# def main():
#     text = 'Bé lên 3 bé đi lớp 4'

    # print(solve(text))
    # assert solve(text) == [3, 4]

#
# if __name__ == "__main__":
#     main()
