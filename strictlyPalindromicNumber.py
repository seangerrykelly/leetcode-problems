# https://leetcode.com/problems/strictly-palindromic-number/description/
class Solution(object):
    def baseTenToOtherBase(self, baseTenInt, base):
        print(base)
        powerOfX = 0
        base = base
        while True:
            minimum = base**powerOfX
            maximum = base**(powerOfX + 1)
            if baseTenInt >= minimum and baseTenInt < maximum:
                break
            powerOfX += 1

        newBaseString = ""
        while True:
            currentSquare = base**powerOfX
            powerOfX -= 1
        
            if baseTenInt - currentSquare >= 0:
                newBaseString = newBaseString + "1"
                baseTenInt -= currentSquare
            else:
                newBaseString = newBaseString + "0"
            
            if powerOfX < 0:
                break
        
        return (newBaseString, baseTenInt == 0)

    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Loop from 2 to n - 2 (inclusive)
        for i in range(2, n-1):
            newBaseString, isNewBasePossible = self.baseTenToOtherBase(n, i)
            if newBaseString != newBaseString[::-1] or isNewBasePossible == False:
                return False
        return True
        