# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos, neg = 0, 0

        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        
        return max(pos, neg)