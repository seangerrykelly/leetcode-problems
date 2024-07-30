# https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Constraints are small. We can do a brute force solution.
        pairs = []
        for i in range(len(nums1)):
            curr1 = nums1[i]
            for j in range(len(nums2)):
                curr2 = nums2[j]
                if curr1 % (curr2*k) == 0:
                    pairs.append((i,j))
        
        return len(pairs)