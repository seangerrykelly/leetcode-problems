class Solution(object):
    
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        perimeter = 0
        visited = {}
        stack = []
        
        for i in range(len(grid)):
            found = False
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    stack.append((i,j))
                    found = True
                    break
            if found is True:
                break
        while stack:
            i,j = stack.pop(0)
            neighbourCount = 0
            
            if visited.get((i,j)) is not None:
                continue
            
            if i - 1 >= 0 and grid[i-1][j] == 1:
                neighbourCount += 1
                stack.append((i-1,j))
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                neighbourCount += 1
                stack.append((i+1,j))
            if j - 1 >= 0 and grid[i][j-1] == 1:
                neighbourCount += 1
                stack.append((i,j-1))
            if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                neighbourCount += 1
                stack.append((i,j+1))
            visited[(i,j)] = True
            perimeter += (4 - neighbourCount)
            
        return perimeter