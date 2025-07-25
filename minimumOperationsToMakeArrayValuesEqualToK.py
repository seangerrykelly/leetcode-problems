# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        distinctMap = {}
        for i in range(len(nums)):
            if nums[i] not in distinctMap:
                distinctMap[nums[i]] = 1
                if nums[i] > k:
                    result += 1
                if nums[i] < k:
                    return -1
            else:
                nums[i] += 1
        
        if len(distinctMap) == 1 and nums[0] == k:
            return 0
        elif result > 0:
            return result
        else:
            return -1