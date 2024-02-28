# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
class Solution(object):
    def removeDuplicates(self, nums):
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
        numKeys = numMap.keys()
        numKeys.sort()
        i = 0
        for num in numKeys:
            numCount = numMap[num]
            maximumCount = 2
            while numCount > 0:
                nums[i] = num
                i += 1
                numCount -= 1
                maximumCount -= 1
                if maximumCount == 0:
                    break
        
        return i