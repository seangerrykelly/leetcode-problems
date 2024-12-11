# https://leetcode.com/problems/hash-divided-string/
class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letterMap = {alphabet[i]: i for i in range(len(alphabet))}
        sums = []
        result = ""

        i = 0
        while i < len(s) - k + 1:
            substring = s[i:i+k]
            i += k
            currSum = 0
            for letter in substring:
                currSum += letterMap[letter]
            sums.append(currSum)
        
        for value in sums:
            result += alphabet[value % 26]

        return result