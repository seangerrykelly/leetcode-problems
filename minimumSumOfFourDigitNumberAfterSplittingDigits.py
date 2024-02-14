# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        minimumSum = 0
        numList = []
        for num in str(num):
            numList.append(int(num))
            
        left, right = 0, len(numList) - 1
        numList.sort()
        
        while left < right:
            firstDigit, secondDigit = numList[left], numList[right]
            minimumSum += (firstDigit * 10) + secondDigit
            left += 1
            right -= 1

        return minimumSum
