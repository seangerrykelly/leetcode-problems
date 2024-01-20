# https://leetcode.com/problems/height-checker/description/
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0

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
        expected = quickSort(heights[:])

        for i in range(len(heights)):
            currHeight, expectedHeight = heights[i], expected[i]
            result = result + 1 if currHeight != expectedHeight else result

        return result
        