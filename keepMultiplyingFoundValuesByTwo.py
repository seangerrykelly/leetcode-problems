# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        numMap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in numMap:
                numMap[num] = i
        
        targetExists = True
        while targetExists:
            if original in numMap:
                original *= 2
            else:
                targetExists = False
        return original