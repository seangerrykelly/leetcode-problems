# https://leetcode.com/problems/powx-n/description/
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x, n)

        # Working solution below except for extreme edge cases
        # result = 1

        # if n == 0:
        #     return result
        # else:
        #     for i in range(abs(n)):
        #         result = result*x

        #     if n < 0:
        #         result = 1/result
        
        # return result
        