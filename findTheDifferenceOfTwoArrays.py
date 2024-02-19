# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1Map, nums2Map = {}, {}
        answer = [[], []]

        for num in nums1:
            if num not in nums1Map:
                nums1Map[num] = 1
        for num in nums2:
            if num not in nums2Map:
                nums2Map[num] = 1
                if num not in nums1Map:
                    answer[1].append(num)
        nums1Map = {}
        for num in nums1:
            if num not in nums1Map:
                nums1Map[num] = 1
                if num not in nums2Map:
                    answer[0].append(num)
        
        return answer

        