# https://leetcode.com/problems/find-indices-of-stable-mountains/description/
class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        stableIndices = []
        for i in range(1, len(height)):
            first, second = height[i-1], height[i]
            if first > threshold:
                stableIndices.append(i)
        
        return stableIndices