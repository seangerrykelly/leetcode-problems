class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        correctIndex = 0
        if target < nums[0]:
            return correctIndex

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                correctIndex = i + 1
                
        return correctIndex
        