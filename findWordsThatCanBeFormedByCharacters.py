# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charMap = {}
        characterCount = 0
        for c in chars:
            if c not in charMap:
                charMap[c] = 1
            else:
                charMap[c] += 1

        for word in words:
            charMapClone = charMap.copy()
            isPossible = True
            for letter in word:
                if letter not in charMapClone:
                    isPossible = False
                    break
                charMapClone[letter] -= 1
                if charMapClone[letter] < 0:
                    isPossible = False
                    break
            if isPossible:
                characterCount += len(word)
        
        return characterCount
