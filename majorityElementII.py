# https://leetcode.com/problems/majority-element-ii/description
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        majorityElements = []
        numMap = {}

        for i in range(len(nums)):
            curr = nums[i]
            if curr not in numMap:
                numMap[curr] = 1
            else:
                numMap[curr] += 1
                
        for num in numMap:
            if numMap[num] > len(nums)/3:
                majorityElements.append(num)
        
        return majorityElements