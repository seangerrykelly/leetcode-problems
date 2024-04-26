# https://leetcode.com/problems/counting-bits/description/
class Solution(object):
    def count1Bits(self, binary):
        oneCount = 0
        for bit in binary:
            if bit == '1':
                oneCount += 1
        return oneCount

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bitCounts = [0 for i in range(n + 1)]

        for i in range(len(bitCounts)):
            bitCounts[i] = self.count1Bits(bin(i)[2:])
        
        return bitCounts