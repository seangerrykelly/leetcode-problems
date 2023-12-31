# https://leetcode.com/problems/most-frequent-even-element/description/
class Solution(object):
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr.pop()
        lower, greater = [], []

        for value in arr:
            if value <= pivot:
                lower.append(value)
            else:
                greater.append(value)
        
        return self.quickSort(lower) + [pivot] + self.quickSort(greater)

    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenNumberMap = {}
        frequency = 0
        for num in nums:
            if num % 2 == 0:
                if num not in evenNumberMap:
                    evenNumberMap[num] = 1
                    if frequency == 0:
                        frequency = 1
                else:
                    evenNumberMap[num] += 1
                    if evenNumberMap[num] > frequency:
                        frequency = evenNumberMap[num]
        
        if len(evenNumberMap) == 0:
            return -1
        
        options = []
        for num in evenNumberMap:
            if evenNumberMap[num] == frequency:
                options.append(num)
        
        return self.quickSort(options)[0]
        
        