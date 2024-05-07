# https://leetcode.com/problems/diagonal-traverse/description/
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Map of indexSum -> row -> val
        cellMap = {}
        diagonalOrder = []
        for i in range(len(nums)):
            row = nums[i]
            for j in range(len(row)):
                cell = row[j]
                indexSum = i + j
                if indexSum not in cellMap:
                    cellMap[indexSum] = {i: row[j]}
                elif i not in cellMap[indexSum]:
                    cellMap[indexSum][i] = row[j]
        
        indexSums = cellMap.keys()
        indexSums.sort()
        for indexSum in indexSums:
            rows = cellMap[indexSum].keys()
            if indexSum % 2 == 0:
                rows.sort(reverse=True)
            else:
                rows.sort()
            for row in rows:
                cell = cellMap[indexSum][row]
                diagonalOrder.append(cell)
        
        return diagonalOrder
