# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05
class Solution(object):
    def buildLetterMap(self, s):
        sMap = {}
        for letter in s:
            if letter not in sMap:
                sMap[letter] = 1
            else:
                sMap[letter] += 1
        return sMap

    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """        
        s1Map, s2Map = self.buildLetterMap(s1), self.buildLetterMap(s2)

        if s1Map != s2Map:
            return False

        mismatchCount = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatchCount += 1
        
            if mismatchCount > 2:
                break
        
        return mismatchCount == 0 or mismatchCount == 2