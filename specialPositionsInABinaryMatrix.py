# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2024-04-02
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        specialCount = 0

        # Map that points row/col index to True/False if special row/col
        rows = {}
        columns = {}
        row1Count = 0
        col1Counts = [0 for i in range(len(mat[0]))]

        # First traverse the matrix and determine which rows and columns are special
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                currCell = mat[i][j]
                if currCell == 1:
                    row1Count += 1
                    col1Counts[j] += 1
                
                if i == len(mat) - 1:
                    # final row, end of column check
                    if col1Counts[j] == 1:
                        columns[j] = True
                    else:
                        columns[j] = False
            
            if row1Count == 1:
                rows[i] = True
            else:
                rows[i] = False
            row1Count = 0
        
        # Traverse the matrix again and count special positions
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                currCell = mat[i][j]
                if currCell == 1 and rows[i] == True and columns[j] == True:
                    specialCount += 1
        
        return specialCount