# https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        jumbleMap = {i: mapping[i] for i in range(len(mapping))}
        sortedMap = {}
        newNums = []
        sortedNums = []
        
        for num in nums:
            numStr = str(num)
            highestPower = len(numStr) - 1
            newNum = 0
            for i in range(len(numStr)):
                digit = int(numStr[i])
                newNum += jumbleMap[digit]*10**highestPower
                highestPower -= 1
            newNums.append(newNum)
            if newNum not in sortedMap:
                sortedMap[newNum] = [num]
            else:
                sortedMap[newNum].append(num)
                
        sortKeys = sortedMap.keys()
        sortKeys.sort()

        for key in sortKeys:
            sortedNums += sortedMap[key]
        
        return sortedNums
