# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
class Solution(object):
    def isObstacle(self, position, obstacleMap):
        if tuple(position) in obstacleMap:
            return True
        return False

    def updatePosition(self, command, position, direction, obstacleMap, positionMap):
        newPosition = list(position)
        for i in range(command):
            if direction == 0:
                # North
                newPosition[1] += 1
                if self.isObstacle(newPosition, obstacleMap):
                    newPosition[1] -= 1
                    break
            elif direction == 90:
                # East
                newPosition[0] += 1
                if self.isObstacle(newPosition, obstacleMap):
                    newPosition[0] -= 1
                    break
            elif direction == 180:
                # South
                newPosition[1] -= 1
                if self.isObstacle(newPosition, obstacleMap):
                    newPosition[1] += 1
                    break
            else:
                # West
                newPosition[0] -= 1
                if self.isObstacle(newPosition, obstacleMap):
                    newPosition[0] += 1
                    break
            if tuple(newPosition) not in positionMap:
                positionMap[tuple(newPosition)] = True
        
        return [tuple(newPosition), positionMap]


    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacleMap = {tuple(obstacles[i]): True for i in range(len(obstacles))}
        positionMap = {(0,0): True}
        currDirection = 0
        currPosition = (0, 0)
        maxDistance = 0

        for command in commands:
            if command == -1:
                currDirection = currDirection + 90 if currDirection != 270 else 0
            elif command == -2:
                currDirection = currDirection - 90 if currDirection != 0 else 270
            else:
                currPosition, positionMap = self.updatePosition(command, currPosition, currDirection, obstacleMap, positionMap)
        
        for position in positionMap:
            distance = position[0]**2 + position[1]**2
            if distance > maxDistance:
                maxDistance = distance

        return maxDistance