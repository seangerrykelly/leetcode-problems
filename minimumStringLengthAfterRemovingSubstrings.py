# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        currIndex = 0
        
        while currIndex < len(s) - 1:
            substr = s[currIndex:currIndex+2]
            if substr == 'AB' or substr == 'CD':
                s = s[:currIndex] + s[currIndex+2:]
                currIndex = currIndex if currIndex == 0 else currIndex - 1
            else:
                currIndex += 1
        
        return len(s)