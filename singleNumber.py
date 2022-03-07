class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counterMap = {}
        for num in nums:
            if num in counterMap:
                counterMap[num] += 1
            else:
                counterMap[num] = 1
                
        for key in counterMap:
            if counterMap[key] == 1:
                return key