# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        numString = str(n)
        numSum, numProduct = 0, 0

        for i in range(len(numString)):
            curr = int(numString[i])
            if i == 0:
                numSum = curr
                numProduct = curr
            else:
                numSum += curr
                numProduct *= curr
        
        return numProduct - numSum