# https://leetcode.com/problems/reshape-the-matrix/description/
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        area = len(mat) * len(mat[0])
        if area != r*c:
            return mat
        orderedVals = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                orderedVals.append(mat[i][j])

        reshapedMat = [[None for i in range(c)] for j in range(r)]
        currIndex = 0
        for i in range(len(reshapedMat)):
            for j in range(len(reshapedMat[i])):
                reshapedMat[i][j] = orderedVals[currIndex]
                currIndex += 1

        return reshapedMat
        
