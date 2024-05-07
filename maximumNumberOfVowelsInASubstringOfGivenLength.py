# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowelMap = {}
        vowels = 'aeiou'
        maxVowelCount = 0
        currVowelCount = 0

        for vowel in vowels:
            vowelMap[vowel] = True
        
        for i in range(0, len(s)-k+1):
            substring = s[i:i+k]
            if i == 0:
                # We only need to check every char of the first substring
                for letter in substring:
                    if letter in vowelMap:
                        currVowelCount += 1
            elif substring[-1] in vowelMap:
                # Then we only need to check first and last chars of every other substring
                currVowelCount += 1
            if currVowelCount > maxVowelCount:
                maxVowelCount = currVowelCount
            if substring[0] in vowelMap:
                currVowelCount -= 1

        return maxVowelCount
