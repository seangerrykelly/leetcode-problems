# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        oddCount = 0
        for num in arr:
            if num % 2 == 0:
                oddCount = 0
            else:
                oddCount += 1
            
            if oddCount == 3:
                return True
        return False