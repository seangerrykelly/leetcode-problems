# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
            
            if numMap[num] >= len(nums)/2.0:
                return num
        