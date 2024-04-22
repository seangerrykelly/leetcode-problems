# https://leetcode.com/problems/find-common-characters/description/
class Solution(object):
    def generateLetterMap(self, word):
        letterMap = {}
        for letter in word:
            if letter not in letterMap:
                letterMap[letter] = 1
            else:
                letterMap[letter] += 1
        return letterMap

    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letterMap = self.generateLetterMap(words.pop(0))
        commonChars = []

        for i in range(len(words)):
            word = words[i]
            currWordMap = self.generateLetterMap(word)
            for letter in letterMap:
                if letter in currWordMap:
                    letterMap[letter] = min(letterMap[letter], currWordMap[letter])
                else:
                    letterMap[letter] = 0
        
        for letter in letterMap:
            letterCount = letterMap[letter]
            letters = [letter for i in range(letterCount)]
            commonChars += letters
            
        return commonChars
                    