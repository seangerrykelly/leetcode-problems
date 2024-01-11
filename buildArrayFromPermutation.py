# https://leetcode.com/problems/build-array-from-permutation/description/
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            curr = nums[i]
            ans.append(nums[curr])
        return ans