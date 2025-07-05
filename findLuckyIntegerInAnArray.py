# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=daily-question&envId=2025-07-05
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        luckyInt = -1
        luckMap = {}

        for num in arr:
            if num not in luckMap:
                luckMap[num] = 1
            else:
                luckMap[num] += 1
        
        for key in luckMap:
            if luckMap[key] == key and key > luckyInt:
                luckyInt = key
        
        return luckyInt