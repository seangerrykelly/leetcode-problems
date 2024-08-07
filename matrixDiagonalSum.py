# https://leetcode.com/problems/matrix-diagonal-sum/description/
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        primarySum, secondarySum = 0, 0
        isOdd = len(mat) % 2 != 0
        i, j = 0, 0
        oddCell = [None, None] if not isOdd else [len(mat)/2, len(mat)/2]

        while i < len(mat):
            # primary diagonal sum
            cell = mat[i][j]
            primarySum += cell
            i += 1
            j += 1
        
        i, j = 0, len(mat) - 1
        while i < len(mat):
            # secondary diagonal sum
            cell = mat[i][j]
            if isOdd and [i,j] == oddCell:
                i += 1
                j -= 1
                continue
            else:
                secondarySum += cell
                i += 1
                j -= 1

        return primarySum + secondarySum
   