# https://leetcode.com/problems/find-the-array-concatenation-value/description/
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concVal = 0
        while len(nums) > 1:
            first = nums.pop(0)
            last = nums.pop()
            currConc = int(str(first) + str(last))
            concVal += currConc
        
        if len(nums) == 1:
            concVal += nums.pop()
        
        return concVal