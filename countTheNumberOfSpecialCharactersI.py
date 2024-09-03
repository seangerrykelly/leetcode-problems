# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        specialCharCount = 0
        alphabetLower = "abcdefghijklmnopqrstuvwxyz"
        alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetMap = {
            'lower': {alphabetLower[i]: 0 for i in range(len(alphabetLower))},
            'upper': {alphabetUpper[j]: 0 for j in range(len(alphabetUpper))}
        }
        specialMap = {}

        for i in range(len(word)):
            if word[i] in alphabetLower:
                alphabetMap['lower'][word[i]] += 1
                if alphabetMap['upper'][word[i].upper()] > 0 and word[i] not in specialMap:
                    specialCharCount += 1
                    specialMap[word[i]] = True
                    specialMap[word[i].upper()] = True
            elif word[i] in alphabetUpper:
                alphabetMap['upper'][word[i]] += 1
                if alphabetMap['lower'][word[i].lower()] > 0 and word[i] not in specialMap:
                    specialCharCount += 1
                    specialMap[word[i]] = True
                    specialMap[word[i].lower()] = True
        
        return specialCharCount