# https://leetcode.com/problems/find-the-distinct-difference-array/description/
class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = []
        prefixMap = {}
        suffixMap = {}

        for i in range(0, len(nums)):
            if nums[i] not in prefixMap:
                prefixMap[nums[i]] = 1
            for j in range(i + 1, len(nums)):
                if nums[j] not in suffixMap:
                    suffixMap[nums[j]] = 1
            diff.append(len(prefixMap) - len(suffixMap))
            suffixMap = {}
        
        return diff