# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-06-11
class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        subarrays = []
        i = 0
        while i < len(nums):
            subarray = nums[i:i+3]
            subarrays.append(subarray)
            i += 3
        
        for subarray in subarrays:
            minimum, maximum = min(subarray), max(subarray)
            if maximum - minimum > k:
                subarrays = []
                break

        return subarrays