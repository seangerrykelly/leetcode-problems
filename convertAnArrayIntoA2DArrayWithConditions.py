# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # The map will be (int) -> (numberOfOccurrences - 1)
        # Whenever int is already a key in the map, append int to the value + 1 and update value
        numMap = {}
        matrix = []

        for num in nums:
            numMap[num] = 0 if num not in numMap else numMap[num] + 1
            if len(matrix) <= numMap[num]:
                matrix.append([])
            matrix[numMap[num]].append(num)

        return matrix