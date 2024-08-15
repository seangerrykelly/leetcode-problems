# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description/
class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        cCount = 0
        for letter in s:
            if letter == c:
                cCount += 1
        
        return cCount * (cCount + 1)/2