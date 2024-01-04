# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
class Solution(object):
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr.pop()
        lower, greater = [], []
        for num in arr:
            if num <= pivot:
                lower.append(num)
            else:
                greater.append(num)
        return self.quickSort(lower) + [pivot] + self.quickSort(greater)

    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kValues = []
        numberMap = {}
        for num in nums:
            if num * -1 in numberMap:
                kValues.append(num if num > 0 else num*-1)
            else:
                numberMap[num] = 1

        if len(kValues) > 0:
            return self.quickSort(kValues)[-1]
        else:
            return -1