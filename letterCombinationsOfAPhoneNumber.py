# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Build map of phone keys to possible letters 
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        phoneMap = {}
        for i in range(2, 10):
            count = 3
            if i == 7 or i == 9:
                count = 4
            substr = alphabet[0:count]
            alphabet = alphabet[count:]
            phoneMap[str(i)] = {substr[j]: True for j in range(len(substr))}

        # Initialize answer array with the length of combinations
        comboCount = 1 if len(digits) > 0 else 0
        comboCounts = []
        maxLetterCount = 3
        if '7' in digits or '9' in digits:
            maxLetterCount = 4
        for i in range(len(digits)):
            letter = digits[i]
            comboCount *= len(phoneMap[letter])
            if len(comboCounts) == 0:
                comboCounts = [comboCount]
            else:
                comboCounts = [comboCount] + comboCounts

        for i in range(len(comboCounts)):
            if i == 0:
                comboCounts[i] /= len(phoneMap[digits[i]])
            elif i < len(comboCounts) - 1:
                comboCounts[i] = comboCounts[i-1] / len(phoneMap[digits[i]])
            else:
                comboCounts[i] = 1
        letterCombos = ["" for i in range(comboCount)]
        remainingCombos = []

        for i in range(len(digits)):
            keys = phoneMap[digits[i]].keys()
            keys.sort()
            currKey = 0
            currComboCount = comboCounts[i]
            for j in range(len(letterCombos)):
                if j % currComboCount == 0:
                    currKey += 1
                    if currKey >= len(keys):
                        currKey = 0
                letterCombos[j] += keys[currKey]
        return letterCombos
        