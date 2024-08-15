# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digitCount = 0
        numStr = str(num)

        for digit in numStr:
            if num % int(digit) == 0:
                digitCount += 1
        
        return digitCount