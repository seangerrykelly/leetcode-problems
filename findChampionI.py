# https://leetcode.com/problems/find-champion-i/description/
class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        candidates = {i: True for i in range(len(grid))}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == j:
                    continue
                if grid[i][j] == 1:
                    candidates[j] = False
                else:
                    candidates[i] = False
        
        for candidate in candidates:
            if candidates[candidate] == True:
                return candidate
        