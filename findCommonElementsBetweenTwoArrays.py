# https://leetcode.com/problems/find-common-elements-between-two-arrays/description/
class Solution(object):
    def buildNumsMap(self, nums):
        numsMap = {}
        for num in nums:
            if num not in numsMap:
                numsMap[num] = True
        return numsMap

    def getAnswer(self, nums, numsMap):
        answer = 0
        for num in nums:
            if num in numsMap:
                answer += 1
        return answer

    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n, m = len(nums1), len(nums2)
        answer = [0, 0]

        nums1Map = self.buildNumsMap(nums1)
        nums2Map = self.buildNumsMap(nums2)
        
        return [self.getAnswer(nums1, nums2Map), self.getAnswer(nums2, nums1Map)]