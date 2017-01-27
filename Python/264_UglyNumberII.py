"""
  264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690. 

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            ugly.append(min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5))
            n -= 1
            if ugly[-1] == ugly[i2]*2:
                i2 += 1
            if ugly[-1] == ugly[i3]*3:
                i3 += 1
            if ugly[-1] == ugly[i5]*5:
                i5 += 1
        return ugly[-1] 