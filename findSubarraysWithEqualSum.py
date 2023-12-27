# https://leetcode.com/problems/find-subarrays-with-equal-sum/submissions/
class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        subarrays = {}
        first, second = 0, 1
        for i in range(len(nums) - 1):
            left, right = nums[first], nums[second]
            subarraySum = left + right
            if subarraySum not in subarrays:
                subarrays[subarraySum] = [[first, second]]
            else:
                return True
            first += 1
            second += 1
        return False