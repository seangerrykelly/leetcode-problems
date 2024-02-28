# https://leetcode.com/problems/sort-colors/description/
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        colorMap = {}
        for num in nums:
            if num not in colorMap:
                colorMap[num] = 1
            else:
                colorMap[num] += 1
        
        i = 0
        for color in colorMap:
            colorCount = colorMap[color]
            while colorCount > 0:
                nums[i] = color
                i += 1
                colorCount -= 1        