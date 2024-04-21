# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            if i == 0:
                currRow = [1]
                triangle.append(currRow)
            else:
                currRow = [1 for j in range(i + 1)]
                for j in range(len(currRow)):
                    if j == 0 or j == len(currRow) - 1:
                        continue
                    newVal = triangle[i-1][j-1] + triangle[i-1][j]
                    currRow[j] = newVal

                triangle.append(currRow)
                
        return triangle

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = self.generate(rowIndex + 1)
        return triangle[rowIndex]
        