# https://leetcode.com/problems/top-k-frequent-words/
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        topKFrequentWords = []
        wordsToFrequencyMap = {}
        for word in words:
            if word not in wordsToFrequencyMap:
                wordsToFrequencyMap[word] = 1
            else:
                wordsToFrequencyMap[word] += 1
        
        frequencyToWordsMap = {}
        for word in wordsToFrequencyMap:
            frequency = wordsToFrequencyMap[word]
            if frequency not in frequencyToWordsMap:
                frequencyToWordsMap[frequency] = [word]
            else:
                frequencyToWordsMap[frequency].append(word)
        
        frequencies = frequencyToWordsMap.keys()
        frequencies.sort(reverse=True)

        for i in range(k):
            currWords = frequencyToWordsMap[frequencies[i]]
            currWords.sort()
            for word in currWords:
                topKFrequentWords.append(word)
                if len(topKFrequentWords) == k:
                    return topKFrequentWords
        
        return topKFrequentWords