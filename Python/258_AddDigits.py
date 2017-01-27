"""
 258. Add Digits


Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = self.sumDigit(num)
        while a >= 10:
            return self.addDigits(a)
        else:
            return a
            
    def sumDigit(self, num):
         result = 0
         for i in str(num):
             result += int(i)
         return result