# https://leetcode.com/problems/sort-the-people/description/
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for x in arr:
                if x <= pivot:
                    lower.append(x)
                else:
                    greater.append(x)
            return quickSort(greater) + [pivot] + quickSort(lower)

        heightMap = {}
        for i in range(len(names)):
            name, height = names[i], heights[i]
            heightMap[height] = name
            
        heights = quickSort(heights)
        sortedNames = []
        for i in range(len(heights)):
            sortedNames.append(heightMap[heights[i]])
        return sortedNames
        