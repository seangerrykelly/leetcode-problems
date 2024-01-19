# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
class Solution(object):
    def checkGrid(self, grid):
        greatestValues = {}
        valuesRemoved = []
        for i in range(len(grid)):
            row = grid[i]
            if i not in greatestValues:
                greatestValues[i] = row[0]
            for j in range(len(row)):
                cell = row[j]
                if cell >= greatestValues[i]:
                    greatestValues[i] = cell
            row.remove(greatestValues[i])
            valuesRemoved.append(greatestValues[i])
        return max(valuesRemoved)

    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        while len(grid[0]) > 0:
            result += self.checkGrid(grid)
        return result