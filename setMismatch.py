# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-05-01
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numMap = {}
        duplicateNum = None
        missingNum = None

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
                duplicateNum = num

        for i in range(1, len(nums) + 1):
            if i not in numMap:
                missingNum = i
        
        return [duplicateNum, missingNum]
        
        