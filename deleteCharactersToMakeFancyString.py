# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2024-11-01
class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        characters = list(s)
        currChar = ""
        charCount = 0
        for i in range(len(characters)):
            c = characters[i]
            if c != currChar:
                currChar = c
                charCount = 0
            charCount += 1
            if charCount >= 3:
                characters[i] = ""
        
        fancyString = "".join(characters)
        return fancyString