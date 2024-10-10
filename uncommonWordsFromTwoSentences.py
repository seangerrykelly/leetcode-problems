class Solution(object):
    def readSentenceAndUpdateMap(self, sentence, wordMap):
        for word in sentence.split():
            if word not in wordMap:
                wordMap[word] = 1
            else:
                wordMap[word] += 1
        return wordMap

    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        uncommonWords = []
        sentenceMap = self.readSentenceAndUpdateMap(s1, {})
        sentenceMap = self.readSentenceAndUpdateMap(s2, sentenceMap)
        
        for word in sentenceMap:
            if sentenceMap[word] == 1:
                uncommonWords.append(word)
        
        return uncommonWords
