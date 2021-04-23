# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# '''
# [Không bắt buộc]
#
# Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
# sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.
#
# Có bao nhiêu đường như vậy trong ô 10x10?
#
# Kiểm tra kết quả bằng https://projecteuler.net/problem=15
# '''
#
#
# def solve(input_data):
#     result = None
#     # Viết code vào đây set result làm kết quả của tính toán
#     #
#     #
#     #
#
#     return result
#
#
# def main():
#     print(solve())
#
#
# if __name__ == "__main__":
#     main()
#http://radiusofcircle.blogspot.com

#http://mathworld.wolfram.com/LatticePath.html

#Import factorial from math module
from math import factorial

#import time from time to calculate exection time
from time import time

#time at the start of execution
start = time()

#binomial coefficient function
#https://en.wikipedia.org/wiki/Binomial_coefficient
def nck(n,k):
	#function which will return the binomial coefficient
	#of n,k
	return factorial(n)/(factorial(k)*factorial(n-k))

#Number of lattice paths from (0,0) to (a,b) is given by
#binomial coefficient C(a+b,a)
print 'Number of lattice paths is: '+str(nck(10+10,10))

#time at the end of program execution
end = time()

#Printing the total time
print end-start