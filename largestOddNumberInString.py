# https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2024-04-07
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in reversed(range(len(num))):
            curr = int(num[i])
            if curr % 2 != 0:
                # num is odd
                result = num[:i+1]
                return result
        
        return ""