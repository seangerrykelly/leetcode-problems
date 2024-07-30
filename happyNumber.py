# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isHappy = False
        numMap = {n: True}
        curr = n

        while True:
            numStr = str(curr)
            newNum = 0

            for digit in numStr:
                newNum += int(digit)**2
            curr = newNum
            if newNum == 1 or newNum == 7:
                isHappy = True
                break
            if newNum not in numMap:
                numMap[newNum] = True
            else:
                break
            
        return isHappy
        