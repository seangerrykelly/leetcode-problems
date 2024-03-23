# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-22
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        pivot = -1
        arr = []
        totalSum = 0
        for i in range(1, n + 1):
            arr.append(i)
            totalSum += i
        
        # Iterate through list keeping track of prefix sum
        prefixSum = 0
        for num in arr:
            prefixSum += num
            suffixSum = totalSum - prefixSum + num
            if prefixSum == suffixSum:
                pivot = num
                break
        
        return pivot