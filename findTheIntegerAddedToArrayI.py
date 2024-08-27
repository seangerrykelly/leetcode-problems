# https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return min(nums2) - min(nums1)