# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []

        firstRow, lastRow = 0, len(matrix)
        firstCol, lastCol = 0, len(matrix[0])
        totalElements = len(matrix) * len(matrix[0])
        currDirection = 'right'

        while totalElements > 0:
            if currDirection == 'right':
                curr = matrix[firstRow]
                for j in range(firstCol, lastCol):
                    spiral.append(curr[j])
                    totalElements -= 1
                firstRow += 1
                lastCol -= 1
                currDirection = 'down'
            elif currDirection == 'down':
                for i in range(firstRow, lastRow):
                    spiral.append(matrix[i][lastCol])
                    totalElements -= 1
                lastRow -= 1
                currDirection = 'left'
            elif currDirection == 'left':
                curr = matrix[lastRow]
                for j in reversed(range(firstCol, lastCol)):
                    spiral.append(curr[j])
                    totalElements -= 1
                currDirection = 'up'
            elif currDirection == 'up':
                for i in reversed(range(firstRow, lastRow)):
                    spiral.append(matrix[i][firstCol])
                    totalElements -= 1
                firstCol += 1
                currDirection = 'right'
        
        return spiral
                
