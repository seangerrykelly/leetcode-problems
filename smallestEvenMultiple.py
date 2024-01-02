# https://leetcode.com/problems/smallest-even-multiple/description/
class Solution(object):
    def isEven(self, n):
        return n % 2 == 0

    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.isEven(n):
            return n
        else:
            return n * 2
