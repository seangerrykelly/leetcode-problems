# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def buildPatternString(self, arr):
        currKey = 0
        patternMap = {}
        for string in arr:
            if string not in patternMap:
                patternMap[string] = currKey
                currKey += 1
        
        patternString = ""
        for string in arr:
            patternString += str(patternMap[string])
        return patternString

    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        patternString = self.buildPatternString(pattern)
        sPattern = self.buildPatternString(s.split())
        
        return patternString == sPattern
        

        

        