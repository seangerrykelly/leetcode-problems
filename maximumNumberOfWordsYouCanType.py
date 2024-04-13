# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        maxNumberOfWords = len(text.split())
        brokenLetterMap = {}

        for letter in brokenLetters:
            if letter not in brokenLetterMap:
                brokenLetterMap[letter] = 1
        
        for word in text.split():
            for letter in word:
                if letter in brokenLetterMap:
                    maxNumberOfWords -= 1
                    break
        
        return maxNumberOfWords