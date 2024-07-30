# https://leetcode.com/problems/hamming-distance/description/
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = bin(x ^ y)[2:]
        hammingDistance = 0
        for i in range(len(xor)):
            if xor[i] == '1':
                hammingDistance += 1

        return hammingDistance
        