class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        numberMap = {}
        for num in nums:
            numberMap[num] = True
        
        for i in range(1, len(nums) + 1):
            if i not in numberMap:
                result.append(i)
        
        return result