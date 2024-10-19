# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        bitSortedArr = []
        bitCountMap = {}
        for i in range(len(arr)):
            binary = bin(arr[i])[2:]
            bitCount = binary.count('1')
            if bitCount not in bitCountMap:
                bitCountMap[bitCount] = [arr[i]]
            else:
                bitCountMap[bitCount].append(arr[i])
        
        bitCounts = bitCountMap.keys()
        bitCounts.sort()

        for bitCount in bitCounts:
            if len(bitCountMap[bitCount]) == 1:
                bitSortedArr += bitCountMap[bitCount]
            else:
                bitCountMap[bitCount].sort()
                bitSortedArr += bitCountMap[bitCount]
        
        return bitSortedArr