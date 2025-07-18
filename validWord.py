# https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowels = 'aeiou'
        hasVowel, hasConsonant = False, False
        word = word.lower()

        if len(word) < 3:
            return False
        
        for i in range(len(word)):
            curr = word[i]
            if curr.isalpha():
                if curr in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True
            elif curr.isdigit():
                continue
            else:
                return False
        
        return hasVowel and hasConsonant
