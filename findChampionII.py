# https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2024-11-26
class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        teamMap = {i: True for i in range(n)}
        for edge in edges:
            loser = edge[1]
            if loser not in teamMap:
                continue
            else:
                del teamMap[loser]
        
        if len(teamMap) != 1:
            return -1

        return teamMap.keys()[0]