class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairCount = 0
        if len(nums) < 2:
            return pairCount
        
        for i in range(len(nums) - 1):
            first = nums[i]
            for j in range(i+1, len(nums)):
                second = nums[j]
                if abs(first - second) == k:
                    pairCount += 1
        return pairCount