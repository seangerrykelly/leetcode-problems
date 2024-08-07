# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = 'aeiou'
        vowelMap = {vowels[i]: True for i in range(len(vowels))}
        likenessMap = {1: 0, 2: 0}
        currHalf = 1

        for i in range(len(s)):
            if i == len(s) / 2:
                currHalf = 2
            letter = s[i].lower()
            if letter in vowelMap:
                likenessMap[currHalf] += 1
        
        return likenessMap[1] == likenessMap[2]
