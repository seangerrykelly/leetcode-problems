# https://leetcode.com/problems/map-sum-pairs/description/
class MapSum(object):

    def __init__(self):
        self.mapSum = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.mapSum[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        prefixLength = len(prefix)
        prefixSum = 0

        for key in self.mapSum:
            if key[0:prefixLength] == prefix:
                prefixSum += self.mapSum[key]
        
        return prefixSum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)