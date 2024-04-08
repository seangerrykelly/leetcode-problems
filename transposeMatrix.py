# https://leetcode.com/problems/transpose-matrix/description/?envType=daily-question&envId=2024-03-23
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])

        transpose = [[0 for i in range(n)] for j in range(m)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                curr = matrix[i][j]
                transpose[j][i] = curr
        
        return transpose