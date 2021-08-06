class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cityMap = {}
        outgoingCityMap = {}
        
        for path in paths:
            departure, arrival = path
            cityMap[departure] = True
            cityMap[arrival] = True
            outgoingCityMap[departure] = True
        
        for city in cityMap:
            if outgoingCityMap.get(city) is None:
                return city