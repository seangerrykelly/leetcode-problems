# https://leetcode.com/problems/path-crossing/description/
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        directionMap = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        pathMap = {0: {0: 1}}
        start = [0, 0]

        for step in path:
            x, y = directionMap[step]
            start[0] += x
            start[1] += y
            if start[0] not in pathMap:
                pathMap[start[0]] = {start[1]: 1}
            elif start[1] not in pathMap[start[0]]:
                pathMap[start[0]][start[1]] = 1
            else:
                return True
        
        return False

