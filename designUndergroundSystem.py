# https://leetcode.com/problems/design-underground-system/description/
class UndergroundSystem(object):

    def __init__(self):
        self.checkInMap = {}
        self.travelTimeMap = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id not in self.checkInMap:
            self.checkInMap[id] = (stationName, t)
        else:
            self.checkInMap[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation = self.checkInMap[id][0]
        travelTime = t - self.checkInMap[id][1]
        if startStation not in self.travelTimeMap:
            self.travelTimeMap[startStation] = {}
        if stationName not in self.travelTimeMap[startStation]:
            self.travelTimeMap[startStation][stationName] = [travelTime, 1.0]
        else:
            self.travelTimeMap[startStation][stationName][0] += travelTime
            self.travelTimeMap[startStation][stationName][1] += 1.0

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        totalTime, customerCount = self.travelTimeMap[startStation][endStation]
        return float(totalTime / customerCount)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)