# https://leetcode.com/problems/reverse-bits/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:]
        zeroCount = 32 - len(binary)
        reversedBits = binary[::-1] + "0"*zeroCount
        return int(reversedBits, 2)