class Solution:
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr.pop()
        valuesLower, valuesGreater = [], []
        
        for num in arr:
            if num < pivot:
                valuesLower.append(num)
            else:
                valuesGreater.append(num)
        
        return self.quickSort(valuesLower) + [pivot] + self.quickSort(valuesGreater)
        
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = self.quickSort(nums)
        result = []
        for i in range(0, len(nums)):
            if nums[i] == target:
                result.append(i)
        return result