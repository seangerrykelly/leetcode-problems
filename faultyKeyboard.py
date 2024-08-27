# https://leetcode.com/problems/faulty-keyboard/description/
class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            if s[i] != 'i':
                result += s[i]
            else:
                result = result[::-1]
        
        return result