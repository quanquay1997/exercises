#!/usr/bin/env python3
# -*- coding: utf-8 -*-
data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)
list1 = len(data[0])
list2 = len(data[1])

def solve(list1):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list1) - 1):
            if list1[i] < list1[i + 1]:
                # Swap the elements
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                # Set the flag to True so we'll loop again
                swapped = True
solve(list1)
print(list1)
    # for i in range(list1):
    #     for j in range(0,list1-i-1):
    #         if list1[j] > list1[j+1]:
    #             list1[j], list1[j+1] = list1[j+1], list1[j]
    # for i in range(list2):
    #     for j in range(0,list2-i-1):
    #         if list2[j] > list2[j+1]:
    #             list2[j], list2[j+1] = list2[j+1], list2[j]
#
# print(1)
# solve(list1)
# for i in range(len(list1)):
#     print ("%d" % list1[i]),
# solve(list2)
# for i in range(len(list2)):
#     print ("%d" % list2[i]),

    # '''Find common elements of two given lists.
    #
    # Returns a list contains those elements.
    # Require: use only lists, if/else and for loops.
    # '''
    # result = []
    #
    # # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result


# def main():
#     for i in data():
#         data([1])
#         L1, L2 = data
#         print(solve(L1, L2))
#
#
# if __name__ == "__main__":
#     main()
