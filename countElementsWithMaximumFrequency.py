# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numToFreqMap = {}
        maxFrequency = 0
        result = 0

        for num in nums:
            if num not in numToFreqMap:
                numToFreqMap[num] = 1
            else:
                numToFreqMap[num] += 1
            
            if numToFreqMap[num] > maxFrequency:
                maxFrequency = numToFreqMap[num]
        
        for num in numToFreqMap:
            if numToFreqMap[num] == maxFrequency:
                result += numToFreqMap[num]
        
        return result
        