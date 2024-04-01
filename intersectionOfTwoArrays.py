# https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=daily-question&envId=2024-03-10
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersectionArr = []
        numMap = {}

        for num in nums1:
            if num not in numMap:
                numMap[num] = 1
        
        for num in nums2:
            if num in numMap:
                intersectionArr.append(num)
                del numMap[num]
        
        return intersectionArr