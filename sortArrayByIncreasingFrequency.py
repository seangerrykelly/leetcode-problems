# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        intToFrequencyMap = {}
        for num in nums:
            if num not in intToFrequencyMap:
                intToFrequencyMap[num] = 1
            else:
                intToFrequencyMap[num] += 1
        
        frequencyToIntMap = {}
        for key in intToFrequencyMap:
            if intToFrequencyMap[key] not in frequencyToIntMap:
                frequencyToIntMap[intToFrequencyMap[key]] = [key]
            else:
                frequencyToIntMap[intToFrequencyMap[key]].append(key)

        frequencies = frequencyToIntMap.keys()
        frequencies.sort()

        for frequency in frequencies:
            frequencyToIntMap[frequency].sort(reverse=True)
            for value in frequencyToIntMap[frequency]:
                curr = [value for i in range(frequency)]
                result += curr
                
        return result


