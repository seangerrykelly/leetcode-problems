# https://leetcode.com/problems/number-of-1-bits/description/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        oneCount = 0
        binary = bin(n)[2:]

        for bit in binary:
            if bit == '1':
                oneCount += 1
        
        return oneCount
        