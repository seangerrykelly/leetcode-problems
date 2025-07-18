# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/
class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        rowMap, colMap = {i: {} for i in range(n)}, {j: {} for j in range(n)}

        # Check every cell and update maps to keep track
        for i in range(n):
            for j in range(n):
                curr = matrix[i][j]
                if curr not in rowMap[i]:
                    rowMap[i][curr] = 1
                else:
                    return False
                if curr not in colMap[j]:
                    colMap[j][curr] = 1
                else:
                    return False
            
            if len(rowMap[i]) != n:
                return False
        
        for col in colMap:
            if len(colMap[col]) != n:
                return False
        
        return True 
