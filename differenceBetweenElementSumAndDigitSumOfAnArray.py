# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementSum = 0
        digitSum = 0

        for num in nums:
            elementSum += num
            numString = str(num)
            for character in numString:
                digitSum += int(character)
        
        result = abs(elementSum - digitSum)
        return result
        