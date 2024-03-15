# https://leetcode.com/problems/minimize-string-length/description/
class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterMap = {}

        for letter in s:
            if letter not in letterMap:
                letterMap[letter] = 1
        
        return len(letterMap)
        