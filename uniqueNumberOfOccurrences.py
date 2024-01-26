# https://leetcode.com/problems/unique-number-of-occurrences/description/
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        frequencyMap = {}
        uniqueOccurrenceMap = {}
        for num in arr:
            if num not in frequencyMap:
                frequencyMap[num] = 1
            else:
                frequencyMap[num] += 1
        
        for num in frequencyMap:
            if frequencyMap[num] not in uniqueOccurrenceMap:
                uniqueOccurrenceMap[frequencyMap[num]] = True
            else:
                return False
                
        return True