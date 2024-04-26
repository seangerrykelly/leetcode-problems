# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]
        prev, curr = None, None

        for i in range(len(binary)):
            curr = binary[i]
            if i == 0:
                prev = curr
                continue
            if curr != prev:
                prev = curr
            else:
                return False
        
        return True
        