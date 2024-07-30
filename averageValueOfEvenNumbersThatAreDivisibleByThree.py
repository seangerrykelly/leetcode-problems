# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        average = 0
        count = 0

        for num in nums:
            if num % 6 == 0:
                average += num
                count += 1
        
        return average if count == 0 else average / count
