# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2024-03-23
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        scores = []
        oneCount = 0
        zeroCount = 0

        for num in s:
            if int(num) == 1:
                oneCount += 1

        for i in range(len(s)):
            num = s[i]
            if int(num) == 0 and i < len(s) - 1:
                zeroCount += 1
            elif int(num) == 1:
                oneCount -= 1

            scores.append(zeroCount + oneCount)
        
        return max(scores)