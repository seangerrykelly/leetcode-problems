
# https://leetcode.com/problems/maximum-odd-binary-number/
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxNumber = ""
        oneCount = 0
        for letter in s:
            if letter == '1':
                oneCount += 1
        
        if oneCount == 1:
            maxNumber = "0"*(len(s)-1) + "1"
        else:
            maxNumber = "1"*(oneCount-1) + "0"*(len(s)-oneCount) + "1"

        return maxNumber