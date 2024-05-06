# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rearrangedNums = []
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        posIndex, negIndex = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos[posIndex]
                posIndex += 1
            else:
                nums[i] = neg[negIndex]
                negIndex += 1
        
        return nums
