# https://leetcode.com/problems/design-neighbor-sum-service/description/
class neighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid
        self.valueMap = {}
        self.n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.valueMap[grid[i][j]] = (i,j)

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        result = 0
        x, y = self.valueMap[value]
        if x > 0:
            result += self.grid[x - 1][y]
        if y > 0:
            result += self.grid[x][y - 1]
        if x < self.n - 1:
            result += self.grid[x+1][y]
        if y < self.n - 1:
            result += self.grid[x][y + 1]
        return result

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        result = 0
        x, y = self.valueMap[value]
        if x > 0 and y > 0:
            result += self.grid[x - 1][y - 1]
        if x < self.n - 1 and y > 0:
            result += self.grid[x + 1][y - 1]
        if x > 0 and y < self.n - 1:
            result += self.grid[x - 1][y + 1]
        if x < self.n - 1 and y < self.n - 1:
            result += self.grid[x + 1][y + 1]
        return result
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)