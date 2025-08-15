# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat == target:
            return True
        
        # First find the transpose of the matrix
        for rotateCount in range(3):
            for i in range(len(mat)):
                # Always start above the diagonal to avoid checking same nums twice
                for j in range(i, len(mat[i])):
                    cell = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = cell
            
            # Reverse each row of the matrix to account for cases where n is even
            for i in range(len(mat)):
                mat[i] = mat[i][::-1]

            # Reverse each row of the matrix to account for cases where n is even
            if mat == target:
                return True
        
        return False