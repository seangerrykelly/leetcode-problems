# https://leetcode.com/problems/k-items-with-the-maximum-sum/description/
class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        maximumSum = 0
        arr = [1 for i in range(numOnes)] + [0 for i in range(numZeros)] + [-1 for i in range(numNegOnes)]
        for i in range(k):
            maximumSum += arr[i]
        return maximumSum