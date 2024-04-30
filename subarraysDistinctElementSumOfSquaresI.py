# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarrays = [nums]
        currLength = 1
        result = 0

        while currLength < len(nums):
            for i in range(0, len(nums)-currLength+1):
                subarray = nums[i:i+currLength]
                subarrays.append(subarray)
            currLength += 1
        
        for subarray in subarrays:
            curr = 0
            distinctMap = {}
            for num in subarray:
                if num not in distinctMap:
                    distinctMap[num] = 1
            result += len(distinctMap)**2
        
        return result
        