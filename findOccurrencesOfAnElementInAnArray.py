# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/
class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        numToIndexMap = {}
        answer = []

        for i in range(len(nums)):
            num = nums[i]
            if num not in numToIndexMap:
                numToIndexMap[num] = [i]
            else:
                numToIndexMap[num].append(i)
        
        if x not in numToIndexMap:
            return [-1 for i in range(len(queries))]
        
        for query in queries:
            if len(numToIndexMap[x]) < query:
                answer.append(-1)
            else:
                answer.append(numToIndexMap[x][query-1])
        
        return answer
        