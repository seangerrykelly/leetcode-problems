# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-09
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        minimumCommon = -1
        numMap = {}

        first, second = 0, 0

        for num in nums1:
            if num not in numMap:
                numMap[num] = 1
        
        for num in nums2:
            if num in numMap:
                minimumCommon = num
                break
        
        return minimumCommon