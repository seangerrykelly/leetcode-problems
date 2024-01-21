# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        lossMap = {}
        winnersAndLosers = [[], []]

        # Map each player ID to their number of losses
        for match in matches:
            winner, loser = match
            if winner not in lossMap:
                lossMap[winner] = 0
            if loser not in lossMap:
                lossMap[loser] = 1
            else:
                lossMap[loser] += 1

        # The values in the output need to be in increasing order
        players = lossMap.keys()
        players.sort()
        
        # Iterate through the map and build the output
        for player in players:
            if lossMap[player] == 0:
                winnersAndLosers[0].append(player)
            elif lossMap[player] == 1:
                winnersAndLosers[1].append(player)
        
        return winnersAndLosers