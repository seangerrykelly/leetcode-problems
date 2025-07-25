# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opCount = 0

        # Constraints are small so we can brute force
        while len(nums) > 0:
            numMap = {}
            isDistinct = True
            for num in nums:
                if num not in numMap:
                    numMap[num] = 1
                else:
                    numMap[num] += 1
                    isDistinct = False
            if isDistinct:
                break
            else:
                for i in range(min(len(nums), 3)):
                    nums.pop(0)
                opCount += 1
        
        return opCount
