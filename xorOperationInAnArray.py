# https://leetcode.com/problems/xor-operation-in-an-array/description/
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [start + 2*i for i in range(n)]
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ nums[i]
        
        return xor