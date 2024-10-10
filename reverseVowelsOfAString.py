# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        vowelMap = {vowels[i]: True for i in range(len(vowels))}
        vowelIndices = []

        for i in range(len(s)):
            if s[i] in vowelMap:
                vowelIndices.append(i)
        
        reverseStr = [s[i] for i in range(len(s))]
        for i in range(len(reverseStr)):
            if reverseStr[i] in vowelMap:
                reverseStr[i] = s[vowelIndices.pop()]

        return "".join(reverseStr)
        