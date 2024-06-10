# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/
class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        keyIndex = -1
        frequencyMap = {}
        mostFrequentNum = None

        for i in range(0, len(nums) - 1):
            if nums[i] == key:
                if mostFrequentNum is None:
                    mostFrequentNum = nums[i+1]
                if nums[i+1] not in frequencyMap:
                    frequencyMap[nums[i+1]] = 1
                else:
                    frequencyMap[nums[i+1]] += 1
                if frequencyMap[nums[i+1]] > frequencyMap[mostFrequentNum]:
                    mostFrequentNum = nums[i+1]

        return mostFrequentNum
