# https://leetcode.com/problems/find-and-replace-pattern/description/
class Solution(object):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def buildPatternMap(self, pattern):
        patternMap = {}
        uniqueCount = 0
        for character in pattern:
            if character not in patternMap:
                patternMap[character] = self.ALPHABET[uniqueCount]
                uniqueCount += 1
        return patternMap
    
    def changeWordToPattern(self, word, patternMap):
        output = ""
        for character in word:
            output += str(patternMap[character])
        return output


    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        patternMap = self.buildPatternMap(pattern)
        patternToMatch = self.changeWordToPattern(pattern, patternMap)
        patternsFound = []

        for word in words:
            wordMap = self.buildPatternMap(word)
            wordPattern = self.changeWordToPattern(word, wordMap)
            if wordPattern == patternToMatch:
                patternsFound.append(word)
        
        return patternsFound