# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result = 0
        for sentence in sentences:
            wordList = sentence.split()
            if len(wordList) > result:
                result = len(wordList)
        
        return result