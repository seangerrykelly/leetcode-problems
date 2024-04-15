# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1232604624/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            currLeft, currRight = numbers[left], numbers[right]
            currSum = currLeft + currRight
            if currSum == target:
                return [left + 1, right + 1]
            elif currSum < target:
                left += 1
            else:
                right -= 1
                