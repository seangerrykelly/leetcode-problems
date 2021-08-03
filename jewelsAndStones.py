class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewelMap = {}
        jewelCount = 0
        
        for jewel in jewels:
            jewelMap[jewel] = True
            
        for stone in stones:
            if jewelMap.get(stone) is None:
                continue
            else:
                jewelCount += 1
        
        return jewelCount