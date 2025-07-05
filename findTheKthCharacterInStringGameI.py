# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=daily-question&envId=2025-07-03
class Solution(object):
    def getNextLetter(self, letter):
        currIndex = self.letterMap[letter]
        if currIndex == 25:
            currIndex = 0
        else:
            currIndex += 1
        return self.alphabet[currIndex]


    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.letterMap = {self.alphabet[i]: i for i in range(len(self.alphabet))}
        word = "a"

        while len(word) < k:
            nextWord = ""
            for i in range(len(word)):
                nextWord += self.getNextLetter(word[i])
            word += nextWord
        
        return word[k - 1]