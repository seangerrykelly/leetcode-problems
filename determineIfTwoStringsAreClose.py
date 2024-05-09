# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-05-08
class Solution(object):
    def getLettersAndFrequencies(self, word):
        letterMap = {}
        for letter in word:
            if letter not in letterMap:
                letterMap[letter] = 1
            else:
                letterMap[letter] += 1
        keys = letterMap.keys()
        values = letterMap.values()
        values.sort()
        keys.sort()
        return (keys, values)

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        lettersAndFrequencies1 = self.getLettersAndFrequencies(word1)
        lettersAndFrequencies2 = self.getLettersAndFrequencies(word2)

        return lettersAndFrequencies1 == lettersAndFrequencies2
