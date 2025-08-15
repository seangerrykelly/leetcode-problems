# https://leetcode.com/problems/count-largest-group/description/
# It's nice solving this one with math instead of casting each number to a string

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        largestGroupCount = 0
        maxGroupSize = 1
        numGroups = {}
        
        for num in reversed(range(1, n + 1)):
            currSum = 0
            while num != 0:
                remainder = num % 10
                currSum += remainder
                num /= 10
            if currSum not in numGroups:
                numGroups[currSum] = [num]
            else:
                numGroups[currSum].append(num)
            
            if len(numGroups[currSum]) > maxGroupSize:
                maxGroupSize = len(numGroups[currSum])
        
        for num in numGroups:
            if len(numGroups[num]) == maxGroupSize:
                largestGroupCount += 1

        return largestGroupCount
