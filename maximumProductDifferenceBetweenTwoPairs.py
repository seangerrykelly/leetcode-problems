# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
class Solution(object):
    def maxProductDifference(self, nums):
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
        result = (nums[len(nums)-1] * nums[len(nums) - 2]) - (nums[0]*nums[1])
        return result