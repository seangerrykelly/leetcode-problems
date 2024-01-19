# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
class Solution(object):
    def checkArithmeticDiffs(self, arr):
        difference = 0
        prev = arr[0]
        arithmeticDiffs = {}
        for i in range(1, len(arr)):
            curr = arr[i]
            difference = curr - prev
            if i == 1:
                arithmeticDiffs[difference] = 1
            elif difference not in arithmeticDiffs:
                return False
            prev = curr
        return True

    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        def quickSort(array, reverse):
            if len(array) <= 1:
                return array
            pivot = array.pop()
            lower, greater = [], []
            for item in array:
                if item <= pivot:
                    lower.append(item)
                else:
                    greater.append(item)
            
            if reverse:
                return quickSort(greater, True) + [pivot] + quickSort(lower, True)
            else:
                return quickSort(lower, False) + [pivot] + quickSort(greater, False)
        
        lowestToGreatest = quickSort(arr[:], False)
        greatestToLowest = quickSort(arr, True)

        return self.checkArithmeticDiffs(lowestToGreatest) and self.checkArithmeticDiffs(greatestToLowest)

        