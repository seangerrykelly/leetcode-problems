# https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-04-07
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isPowerOfTwo = False
        remainder = n

        if n == 1:
            return True
        
        if n <= 0:
            return False

        while remainder > 0:
            if remainder % 2 != 0:
                break
            remainder = remainder / 2
            if remainder == 1:
                isPowerOfTwo = True
                break
            
        return isPowerOfTwo