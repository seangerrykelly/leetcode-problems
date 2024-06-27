# https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        sortMap = {}
        leftoverNums = []

        for i in range(len(arr2)):
            if arr2[i] not in sortMap:
                sortMap[arr2[i]] = i
        
        i = 0
        while i < len(arr1):
            if arr1[i] not in sortMap:
                leftoverNums.append(arr1.pop(i))
            else:
                i += 1
        leftoverNums.sort()

        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []

            for num in arr:
                if sortMap[num] <= sortMap[pivot]:
                    lower.append(num)
                else:
                    greater.append(num)
            return quick_sort(lower) + [pivot] + quick_sort(greater)
        arr1 = quick_sort(arr1)

        return arr1 + leftoverNums
