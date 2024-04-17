# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        totalSum = 0

        for i in range(len(nums)):
            binaryString = str(bin(i))
            kCount = 0
            # Ignore the first two characters since all numbers are positive
            for character in binaryString[2:]:
                if character == '1':
                    kCount += 1
            if kCount == k:
                totalSum += nums[i]

        return totalSum
        