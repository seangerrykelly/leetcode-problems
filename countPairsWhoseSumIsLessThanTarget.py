# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0

        if len(nums) == 1:
            return count

        # Brute force solution
        for i in range(len(nums)):
            currLeft = nums[i]
            for j in range(i + 1, len(nums)):
                currRight = nums[j]
                if currLeft + currRight < target:
                    count += 1
        
        return count