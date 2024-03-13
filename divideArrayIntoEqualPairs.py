# https://leetcode.com/problems/divide-array-into-equal-pairs/
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = True
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
        
        for num in numMap:
            if numMap[num] % 2 != 0:
                result = False
                break
        
        return result

        