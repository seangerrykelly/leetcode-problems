# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        subarrays = []
        currLength = 1
        oddSum = 0

        while currLength <= len(arr):
            for i in range(0, len(arr)-currLength+1):
                subarray = arr[i:i+currLength]
                subarrays.append(subarray)
            currLength += 2

        for subarray in subarrays:
            for num in subarray:
                oddSum += num

        return oddSum
