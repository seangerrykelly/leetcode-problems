# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortedNums = nums[:]
        sortedNums.sort()

        # Find min value in sortedNums, then check values
        minIndex = 0
        for i in range(len(nums)):
            if nums[i] == sortedNums[0]:
                minIndex = i
                nums = nums[i:] + nums[:i]

        
        return nums == sortedNums