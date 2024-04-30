# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        negCount = 0
        
        for row in grid:
            for cell in row:
                if cell < 0:
                    negCount += 1
        
        return negCount
