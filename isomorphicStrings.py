# https://leetcode.com/problems/isomorphic-strings/description/?envType=daily-question&envId=2024-04-02
class Solution(object):
    def generateOrderString(self, word):
        letterMap = {}
        currIndex = 1
        newWord = ""
        for i in range(len(word)):
            letter = word[i]
            if letter not in letterMap:
                letterMap[letter] = currIndex
                currIndex += 1
            newWord += str(letterMap[letter])
        return newWord

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.generateOrderString(s) == self.generateOrderString(t)

        