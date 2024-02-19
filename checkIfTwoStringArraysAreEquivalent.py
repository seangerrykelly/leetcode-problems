# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        def buildStringFromArray(word):
            strToReturn = ''
            for segment in word:
                strToReturn += segment
            return strToReturn

        word1Str = buildStringFromArray(word1)
        word2Str = buildStringFromArray(word2)
        
        return word1Str == word2Str