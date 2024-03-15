# https://leetcode.com/problems/two-out-of-three/description/
class Solution(object):
    def updateNumMap(self, nums, numMap):
        distinctMap = {}
        
        for num in nums:
            if num not in distinctMap:
                distinctMap[num] = 1
                if num not in numMap:
                    numMap[num] = 1
                else:
                    numMap[num] += 1

        return numMap

    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        numMap = {}
        twoOutOfThree = []
        numMap = self.updateNumMap(nums1, numMap)
        numMap = self.updateNumMap(nums2, numMap)
        numMap = self.updateNumMap(nums3, numMap)

        for num in numMap:
            curr = numMap[num]
            if curr >= 2:
                twoOutOfThree.append(num)

        return twoOutOfThree
        