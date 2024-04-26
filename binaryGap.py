# https://leetcode.com/problems/binary-gap/description/
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        start, end = None, None
        maxGap = 0

        for i in range(len(binary)):
            bit = binary[i]
            if bit == '1':
                if start == None:
                    start = i
                else:
                    end = i
                    gap = end - start
                    if gap > maxGap:
                        maxGap = gap
                    start = i
        return maxGap


                