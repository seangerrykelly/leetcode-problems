# https://leetcode.com/problems/maximum-69-number/description/
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        numArray = list(str(num))
        numString = ''
        hasChangedDigit = False
        for i in range(len(numArray)):
            if numArray[i] == '6' and hasChangedDigit == False:
                numArray[i] = '9'
                hasChangedDigit = True
            numString += numArray[i]
        
        return int(numString)