# https://leetcode.com/problems/third-maximum-number/description/
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {nums[i]: True for i in range(len(nums))}
        distinctNums = numMap.keys()
        
        if len(distinctNums) < 3:
            return max(distinctNums)
        
        distinctNums.sort()
        return distinctNums[-3]