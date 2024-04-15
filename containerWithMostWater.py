# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            currLeft, currRight = height[left], height[right]
            currHeight = min(currLeft, currRight)
            currBase = right - left
            currArea = currHeight * currBase
            if currArea > maxArea:
                maxArea = currArea
            if currLeft <= currRight:
                left += 1
            else:
                right -= 1
        
        return maxArea