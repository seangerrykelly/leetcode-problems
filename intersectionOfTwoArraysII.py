# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02
class Solution(object):
    def buildNumMap(self, nums):
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
        return numMap

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        num1Map, num2Map = self.buildNumMap(nums1), self.buildNumMap(nums2)

        for num in num1Map:
            if num in num2Map:
                count = min(num1Map[num], num2Map[num])
                intersection += [num for x in range(count)]
        
        return intersection
        