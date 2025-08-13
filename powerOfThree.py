# https://leetcode.com/problems/power-of-three/description/?envType=daily-question&envId=2025-08-13
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        exponent = 0
        power = 0

        while power < n:
            power = 3**exponent
            exponent += 1
            if power == n:
                return True
        
        return False
