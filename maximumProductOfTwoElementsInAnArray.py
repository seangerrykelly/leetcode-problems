# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for item in arr:
                if item <= pivot:
                    lower.append(item)
                else:
                    greater.append(item)
            
            return quickSort(lower) + [pivot] + quickSort(greater)
        
        nums = quickSort(nums)
        result = (nums[len(nums)-1] - 1) * (nums[len(nums)-2] - 1)
        return result