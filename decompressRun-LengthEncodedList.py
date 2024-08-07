# https://leetcode.com/problems/decompress-run-length-encoded-list/description/
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        decompList = []
        i = 0

        while i < len(nums) - 1:
            freq, val = nums[i], nums[i+1]
            i += 2

            for j in range(freq):
                decompList.append(val)
        
        return decompList
        