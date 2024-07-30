# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opCount = 0
        for num in nums:
            if num % 3 == 0:
                continue
            opCount += 1
        
        return opCount
