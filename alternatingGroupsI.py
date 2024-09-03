# https://leetcode.com/problems/alternating-groups-i/description/
class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        groupCount = 0

        for i in range(len(colors)):
            currTile = colors[i]
            if i == 0:
                prevTile = colors[-1]
                nextTile = colors[i+1]
            elif i == len(colors) - 1:
                prevTile = colors[i-1]
                nextTile = colors[0]
            else:
                prevTile = colors[i-1]
                nextTile = colors[i+1]
            if currTile != prevTile and currTile != nextTile:
                groupCount += 1
        
        return groupCount
        