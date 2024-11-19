# https://leetcode.com/problems/maximum-xor-for-each-query/?envType=daily-question&envId=2024-11-08
class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        xorMax = (2**maximumBit) - 1
        queries = []
        xor = 0

        for i in range(len(nums)):
            curr = nums[i]
            xor ^= curr
            k = xor ^ xorMax
            queries.append(k)
        
        queries.reverse()
        return queries