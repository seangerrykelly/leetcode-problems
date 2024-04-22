# https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        targetRow = 0
        prev, curr = None, None
        for i in range(len(matrix)):
            if i == 0:
                prev = matrix[i][0]
            else:
                curr = matrix[i][0]
                if target < curr:
                    targetRow = i - 1
                    break
                elif target > curr:
                    prev = curr
                    targetRow = i
                    continue
                else:
                    return True
        
        for i in range(len(matrix[targetRow])):
            cell = matrix[targetRow][i]
            if cell == target:
                return True
        
        return False

