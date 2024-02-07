# https://leetcode.com/problems/shuffle-the-array/description/
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return nums
        xIndex, yIndex = 1, (len(nums)/2)
        xNums = nums[0:n]
        yNums = nums[n:]
        i = 0
        currIndex = 0
        while i < len(nums):
            nums[i] = xNums[currIndex]
            nums[i + 1] = yNums[currIndex]
            i += 2
            currIndex += 1

        return nums