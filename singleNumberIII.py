# https://leetcode.com/problems/single-number-iii/description/?envType=daily-question&envId=2024-05-31
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            for j in range(i+1, len(nums)):
                if nums[i] ^ nums[j] == 0:
                    nums.pop(i)
                    nums.pop(j - 1)
                    i = -1
                    break
            i += 1

        return nums