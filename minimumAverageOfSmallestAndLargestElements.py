# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages = []
        while len(nums) > 0:
            minIndex = nums.index(min(nums))
            minElement = nums.pop(minIndex)
            maxIndex = nums.index(max(nums))
            maxElement = nums.pop(maxIndex)
            average = (minElement + maxElement) / 2.0
            averages.append(average)
        
        return min(averages)
