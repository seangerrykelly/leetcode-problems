# https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # First find the transpose of the matrix
        for i in range(len(matrix)):
            # Always start above the diagonal to avoid checking same nums twice
            for j in range(i, len(matrix[i])):
                cell = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = cell
        
        # Reverse each row of the matrix to account for cases where n is even
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]