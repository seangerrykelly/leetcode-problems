# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/
class Solution(object):
    def buildAlphabetMap(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabetMap = {}
        for i in range(len(alphabet)):
            alphabetMap[alphabet[i]] = i
        return alphabetMap

    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabetMap = self.buildAlphabetMap()
        longestSubstringLength = 0
        curr, prev = '', ''
        substring = ''
        substrings = []
        
        for i in range(len(s)):
            curr = s[i]
            if len(substring) == 0:
                substring = curr
            elif alphabetMap[curr] - alphabetMap[prev] == 1:
                substring += curr
            else:
                substrings.append(substring)
                substring = curr
            prev = curr
        if len(substring) != 0:
            substrings.append(substring)

        for item in substrings:
            if len(item) > longestSubstringLength:
                longestSubstringLength = len(item)
        return longestSubstringLength



            
            
