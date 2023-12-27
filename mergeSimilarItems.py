# https://leetcode.com/problems/merge-similar-items/submissions/
class Solution(object):
    def generateWeightMap(self, items, weightMap):
        for item in items:
            if item[0] not in weightMap:
                weightMap[item[0]] = item[1]
            else:
                weightMap[item[0]] += item[1]
        return weightMap

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

    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        weightMap = {}
        weightMap = self.generateWeightMap(items1, weightMap)
        weightMap = self.generateWeightMap(items2, weightMap)
        
        values = self.quickSort(weightMap.keys())
        ret = []

        for i in range(len(values)):
            weight = weightMap[values[i]]
            ret.append([values[i], weight])
        return ret
        