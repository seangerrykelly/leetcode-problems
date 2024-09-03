# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabetMap = {alphabet[i]: i+1 for i in range(len(alphabet))}
        numString = ""
        for i in range(len(s)):
            numString += str(alphabetMap[s[i]])
        
        result = 0
        while k > 0:
            k -= 1
            currSum = 0
            for i in range(len(numString)):
                currSum += int(numString[i])
            numString = str(currSum)
            result = currSum

        return result
