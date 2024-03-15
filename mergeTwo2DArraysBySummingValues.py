# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
class Solution(object):
    def updateSumMap(self, nums, sumMap):
        for num in nums:
            currId, currValue = num
            if currId not in sumMap:
                sumMap[currId] = currValue
            else:
                sumMap[currId] += currValue
        
        return sumMap

    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        sumMap = {}
        sumMap = self.updateSumMap(nums1, sumMap)
        sumMap = self.updateSumMap(nums2, sumMap)
        arrayIds = sumMap.keys()
        arrayIds.sort()
        
        mergedArray = []

        for arrayId in arrayIds:
            pair = [arrayId, sumMap[arrayId]]
            mergedArray.append(pair)
        
        return mergedArray
        