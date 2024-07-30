# https://leetcode.com/problems/toeplitz-matrix/description/
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            if i == 0:
                continue
            for j in range(len(matrix[i])):
                if j == 0:
                    continue
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        
        return True
