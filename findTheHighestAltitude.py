# https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        hightestIndex = 0
        currAltitude = 0
        maxAltitude = None
        gain = [0] + gain

        for i in range(len(gain)):
            currGain = gain[i]
            currAltitude += currGain
            if maxAltitude is None or currAltitude > maxAltitude:
                maxAltitude = currAltitude
        
        return maxAltitude
        