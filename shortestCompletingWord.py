# https://leetcode.com/problems/shortest-completing-word/description/
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letterMap = {}
        completingWords = []

        # Build map of letters pointing to their counts
        for letter in licensePlate:
            if letter.isalpha():
                if letter.lower() not in letterMap:
                    letterMap[letter.lower()] = 1
                else:
                    letterMap[letter.lower()] += 1
        
        # Build map for each word and compare with letterMap
        for word in words:
            wordMap = {}
            for letter in word:
                if letter not in wordMap:
                    wordMap[letter] = 1
                else:
                    wordMap[letter] += 1
            isPossible = True
            for letter in letterMap:
                if letter not in wordMap or letterMap[letter] > wordMap[letter]:
                    isPossible = False
                    break
            if isPossible:
                completingWords.append(word)

        # Find shortest item in completingWords
        shortestWord = None
        for i in range(len(completingWords)):
            word = completingWords[i]
            print(word)
            if shortestWord is None:
                shortestWord = word
            if len(word) < len(shortestWord):
                shortestWord = word
        
        return shortestWord
        