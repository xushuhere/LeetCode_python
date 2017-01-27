"""
 7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        str_x= str(abs(x))
        result = ''
        for i in str_x:
            result = i + result
        result = int(result)
        if result > 0x7fffffff:
            return 0
        else:
            return sign * result
        