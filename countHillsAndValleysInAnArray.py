# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27
class Solution(object):
    def isHill(self, left, curr, right):
        if curr > left and curr > right:
            return True
        return False

    def isValley(self, left, curr, right):
        if curr < left and curr < right:
            return True
        return False

    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        left, curr, right = None, None, None

        while i < len(nums) - 1:
            if i == 0:
                left = nums[i]
                i += 1
                continue
            curr = nums[i]
            right = nums[i+1]
            if self.isHill(left, curr, right) or self.isValley(left, curr, right):
                count += 1
                left = curr
            i += 1
        
        return count

