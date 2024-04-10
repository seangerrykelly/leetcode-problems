# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2024-04-10
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = -1
        distanceMap = {}

        for i in range(len(s)):
            letter = s[i]
            if letter not in distanceMap:
                distanceMap[letter] = (i, None)
            else:
                distanceMap[letter] = (distanceMap[letter][0], i)
        
        for letter in distanceMap:
            if distanceMap[letter][1] == None:
                continue
            start, end = distanceMap[letter]
            substring = s[start+1:end]
            if len(substring) > maxLength:
                maxLength = len(substring)
        
        return maxLength