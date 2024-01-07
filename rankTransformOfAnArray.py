# https://leetcode.com/problems/rank-transform-of-an-array/description/
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def quickSort(array):
            if len(array) <= 1:
                return array
            pivot = array.pop()
            lower, greater = [], []
            
            for num in array:
                if num <= pivot:
                    lower.append(num)
                else:
                    greater.append(num)
        
            return quickSort(lower) + [pivot] + quickSort(greater)

        sortedArr = quickSort(arr[:])
        rankMap = {}
        rankCounter = 1

        # Build map of rankings using the sorted array
        for i in range(len(sortedArr)):
            if i == 0:
                rankMap[sortedArr[i]] = rankCounter
                rankCounter += 1
            else:
                if sortedArr[i] not in rankMap:
                    rankMap[sortedArr[i]] = rankCounter
                    rankCounter += 1
                else:
                    continue

        # Iterate through original array and replace every value with rank
        for i in range(len(arr)):
            arr[i] = rankMap[arr[i]]
        
        return arr