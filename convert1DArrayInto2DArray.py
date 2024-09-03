# https://leetcode.com/problems/convert-1d-array-into-2d-array/?envType=daily-question&envId=2024-09-01
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m * n != len(original):
            return []

        originalIter = iter(original)
        arr = [[None for i in range(n)] for j in range(m)]
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = next(originalIter)
        
        return arr