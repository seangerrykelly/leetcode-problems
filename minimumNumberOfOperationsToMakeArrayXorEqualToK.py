# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/?envType=daily-question&envId=2024-06-05
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        opCount = 0
        xor = 0
        for num in nums:
            xor = xor ^ num

        for bit in bin(xor ^ k):
            if bit == '1':
                opCount += 1

        return opCount