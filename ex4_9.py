#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve(numbers):
    '''Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`
    '''
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                # Swap the elements
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # Set the flag to True so we'll loop again
                swapped = True
listnumber = [-1, 5, 9, 6, 2, 1]
solve(listnumber)
print(listnumber)
    # assert isinstance(numbers, list)
    # result = None

    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result


# def main():
#     for i in range(solve):
#         for i
#         print(solve([-1, 5, 9, 6, 2, 1]))
#
#
# if __name__ == "__main__":
#     main()
