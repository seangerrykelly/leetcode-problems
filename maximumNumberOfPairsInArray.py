# https://leetcode.com/problems/maximum-number-of-pairs-in-array/submissions/
class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairCount, leftoverCount = 0, 0
        pairMap = {}
        for num in nums:
            if num not in pairMap:
                pairMap[num] = 1
            else:
                pairMap[num] += 1

        for pair in pairMap:
            currPairCount = pairMap[pair]
            if currPairCount > 1:
                pairCount += currPairCount / 2
                leftoverCount += currPairCount % 2
            else:
                leftoverCount += 1
        
        return [pairCount, leftoverCount]