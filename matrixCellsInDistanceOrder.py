# https://leetcode.com/problems/matrix-cells-in-distance-order/description/
class Solution(object):
    def calculateDistance(self, cell, center):
        """
        :type cell: List[List[int]]
        :type center: List[List[int]]
        :rtype: int
        """
        return abs(cell[0] - center[0]) + abs(cell[1] - center[1])

    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        distanceMap = {}
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        distanceOrder = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                distance = self.calculateDistance([i, j], [rCenter, cCenter])
                if distance not in distanceMap:
                    distanceMap[distance] = [[i,j]]
                else:
                    distanceMap[distance].append([i,j])
        
        distances = distanceMap.keys()
        distances.sort()
        for distance in distances:
            distanceOrder += distanceMap[distance]

        return distanceOrder