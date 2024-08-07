# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        maxWidth = 0
        pointMap = {}
        for point in points:
            x, y = point
            if x not in pointMap:
                pointMap[x] = [y]
            else:
                pointMap[x].append(y)
        
        keys = pointMap.keys()
        keys.sort()

        for i in range(0, len(keys) - 1):
            start, end = keys[i], keys[i+1]
            verticalArea = end - start
            if verticalArea > maxWidth:
                maxWidth = verticalArea

        return maxWidth