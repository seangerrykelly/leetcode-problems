# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/
class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversedS = s[::-1]
        for i in range(0, len(s) - 1):
            substr = s[i:i+2]
            if substr in reversedS:
                return True
        
        return False
        