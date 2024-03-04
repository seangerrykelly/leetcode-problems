# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maximumCandyCount = max(candies)

        for kid in candies:
            if kid + extraCandies >= maximumCandyCount:
                result.append(True)
            else:
                result.append(False)
        
        return result