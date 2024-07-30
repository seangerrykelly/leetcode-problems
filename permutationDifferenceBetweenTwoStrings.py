# https://leetcode.com/problems/permutation-difference-between-two-strings/description/
class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        permutationDifference = 0
        sMap = {}
        for i in range(len(s)):
            letter = s[i]
            sMap[letter] = i
        
        for i in range(len(t)):
            letter = t[i]
            permutationDifference += abs(sMap[letter] - i)

        return permutationDifference
        