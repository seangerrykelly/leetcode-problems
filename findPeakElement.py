# https://leetcode.com/problems/find-peak-element/description/
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        left, curr, right = None, None, None

        if len(nums) == 1:
            return 0

        while i < len(nums):
            curr = nums[i]
            if i == 0:
                # Only care about right
                right = nums[i + 1]
                if curr > right:
                    peak = i
                    break
            elif i == len(nums) - 1:
                # Only care about left
                left = nums[i - 1]
                if curr > left:
                    peak = i
                    break
            else:
                # Care about both neighbours
                left = nums[i - 1]
                right = nums[i + 1]
                if curr > left and curr > right:
                    peak = i
                    break
            i += 1
        
        return i