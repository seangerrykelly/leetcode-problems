# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterMap = {}
        currMax = 0
        currLength = 0
        i = 0

        while i < len(s):
            letter = s[i]
            if letter not in letterMap:
                letterMap[letter] = i
                currLength += 1
                i += 1
            else:
                i = letterMap[letter] + 1
                letterMap = {}
                currLength = 0
                continue
            if currLength > currMax:
                currMax = currLength
        return currMax  
            