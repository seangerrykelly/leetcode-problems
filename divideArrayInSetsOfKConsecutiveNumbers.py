# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
        
        while len(numMap) > 0:
            subarray = []
            minNum = min(numMap.keys())
            for i in range(k):
                if minNum not in numMap:
                    return False
                else:
                    subarray.append(minNum)
                    numMap[minNum] -= 1
                
                if numMap[minNum] == 0:
                    del numMap[minNum]
                minNum += 1
                
        return True    