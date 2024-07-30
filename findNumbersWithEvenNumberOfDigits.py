# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenCount = 0

        for num in nums:
            power = log10(num)
            digitCount = int(power + 1)
            if digitCount % 2 == 0:
                evenCount += 1
        
        return evenCount