class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        harshadNumber = 0
        for digit in str(x):
            harshadNumber += int(digit)
        
        if x % harshadNumber == 0:
            return harshadNumber
        return -1