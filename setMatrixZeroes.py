# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroMap = {'cols': {}, 'rows': {}}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroMap['rows'][i] = 1
                    zeroMap['cols'][j] = 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in zeroMap['rows'] or j in zeroMap['cols']:
                    matrix[i][j] = 0