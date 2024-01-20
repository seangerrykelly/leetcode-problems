# https://leetcode.com/problems/neither-minimum-nor-maximum/description/
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -1
        if len(nums) <= 2:
            return result
        
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for num in arr:
                if num <= pivot:
                    lower.append(num)
                else:
                    greater.append(num)
            return quickSort(lower) + [pivot] + quickSort(greater)
            
        result = quickSort(nums)[1]
        return result