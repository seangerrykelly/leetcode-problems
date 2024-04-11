# https://leetcode.com/problems/points-that-intersect-with-cars/description/
class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        pointMap = {}
        maxValue = 0
        result = 0

        for num in nums:
            start, end = num
            for i in range(start, end + 1):
                if i > maxValue:
                    maxValue = i
                if i not in pointMap:
                    pointMap[i] = 1
        
        for i in range(maxValue + 1):
            if i not in pointMap:
                continue
            else:
                result += 1
        
        return result
            