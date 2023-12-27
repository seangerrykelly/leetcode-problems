# https://leetcode.com/problems/check-distances-between-same-letters/description/
class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        distanceMap = {}
        n = len(s)
        for i in range(n):
            if s[i] not in distanceMap:
                distanceMap[s[i]] = i + 1
            else:
                distanceMap[s[i]] = i - distanceMap[s[i]]

        for i in range(len(distance)):
            letter = alphabet[i]
            currDistance = distance[i]
            if letter not in distanceMap:
                continue
            elif currDistance != distanceMap[letter]:
                return False
        return True
