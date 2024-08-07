# https://leetcode.com/problems/equal-row-and-column-pairs/description/
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pairCount = 0
        rowMap = {}
        colMap = {}
        columns = [[] for i in range(len(grid))]
        for i in range(len(grid)):
            currRow = []
            for j in range(len(grid[i])):
                currRow.append(grid[i][j])
                columns[j].append(grid[i][j])
            rowMap[i] = tuple(currRow)
        
        for column in columns:
            currCol = tuple(column)
            if currCol not in colMap:
                colMap[currCol] = 1
            else:
                colMap[currCol] += 1

        for row in rowMap:
            if rowMap[row] in colMap:
                pairCount += colMap[rowMap[row]]
        
        return pairCount
        