# https://leetcode.com/problems/power-of-four/description/
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        exponent = 0
        power = 0

        while power < n:
            power = 4**exponent
            exponent += 1
            if power == n:
                return True
        
        return False