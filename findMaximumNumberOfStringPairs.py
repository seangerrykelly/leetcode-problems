# https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/
class Solution(object):
    def reverseString(self, word):
        return word[::-1]

    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordMap = {}
        pairMap = {}

        for word in words:
            if word not in wordMap:
                wordMap[word] = 1
        
        for word in wordMap:
            reversedWord = self.reverseString(word)
            # words are all distinct, so we can ignore cases where word == reversedWord
            if word == reversedWord:
                continue
            if reversedWord in wordMap:
                # Check if you've already counted it
                if word in pairMap or reversedWord in pairMap:
                    continue
                else:
                    pairMap[word] = 1
        
        return len(pairMap)
        

        