# https://leetcode.com/problems/merge-sorted-array/description/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        numsMap = {}

        for i in range(m):
            if nums1[i] not in numsMap:
                numsMap[nums1[i]] = 1
            else:
                numsMap[nums1[i]] += 1
        
        for i in range(n):
            if nums2[i] not in numsMap:
                numsMap[nums2[i]] = 1
            else:
                numsMap[nums2[i]] += 1
        
        nums = numsMap.keys()
        nums.sort()
        currNum = 0
        
        for i in range(n + m):
            if numsMap[nums[currNum]] > 0:
                nums1[i] = nums[currNum]
                numsMap[nums[currNum]] -= 1
            
            if numsMap[nums[currNum]] == 0:
                currNum += 1
        