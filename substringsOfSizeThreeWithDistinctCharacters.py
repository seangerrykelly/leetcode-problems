# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        goodCount = 0

        for i in range(len(s) - 2):
            letterMap = {}
            isGood = True
            substr = s[i:i+3]

            for letter in substr:
                if letter not in letterMap:
                    letterMap[letter] = 1
                else:
                    isGood = False
                    break
            goodCount = goodCount + 1 if isGood else goodCount
        
        return goodCount