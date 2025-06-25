# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        pairCount = 0
        dominoMap = {}

        for domino in dominoes:
            curr = tuple(domino)
            currRotated = curr[::-1]

            if currRotated in dominoMap:
                pairCount += dominoMap[currRotated]
                if curr[0] == curr[1]:
                    dominoMap[curr] += 1
                    continue

            if curr not in dominoMap:
                dominoMap[curr] = 1
            else:
                pairCount += dominoMap[curr]
                dominoMap[curr] += 1

        return pairCount