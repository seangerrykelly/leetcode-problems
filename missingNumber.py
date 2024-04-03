# https://leetcode.com/problems/missing-number/description/?envType=daily-question&envId=2024-04-02
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fullArray = [i for i in range(0, len(nums) + 1)]

        correctSum = 0
        incorrectSum = 0
        for i in range(len(fullArray)):
            correctSum += fullArray[i]
        for i in range(len(nums)):
            incorrectSum += nums[i]
        
        return correctSum - incorrectSum

