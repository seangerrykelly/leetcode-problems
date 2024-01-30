# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int] 
        """
        duplicateMap = {}
        duplicateList = []
        for num in nums:
            if num not in duplicateMap:
                duplicateMap[num] = 1
            else:
                duplicateList.append(num)
        
        return duplicateList