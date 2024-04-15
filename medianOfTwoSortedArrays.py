# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        count = 0
        isEven = total % 2 == 0
        stack = []
        i, j = 0, 0

        while True:
            if i < len(nums1) and j < len(nums2):
                curr1, curr2 = nums1[i], nums2[j]
                if curr1 > curr2:
                    j += 1
                    count += 1
                    stack.append(curr2)
                else:
                    i += 1
                    count += 1
                    stack.append(curr1)
            elif i < len(nums1):
                curr1 = nums1[i]
                i += 1
                count += 1
                stack.append(curr1)
            elif j < len(nums2):
                curr2 = nums2[j]
                j += 1
                count += 1
                stack.append(curr2)
            if isEven and count == (total / 2) + 1:
                median1 = stack.pop()
                median2 = stack.pop()
                return (median1 + median2) / 2.0
            elif isEven == False and count == (total/2) + 1:
                return stack.pop()
