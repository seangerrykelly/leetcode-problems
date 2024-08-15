# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        flipCount = 0
        xor = start ^ goal
        binaryXor = bin(xor)[2:]

        for bit in binaryXor:
            if bit == '1':
                flipCount += 1

        return flipCount