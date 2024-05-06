# https://leetcode.com/problems/create-target-array-in-the-given-order/description/
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = [-1 for i in range(len(nums))]

        for i in range(len(index)):
            targetIndex = index[i]
            targetNum = nums[i]
            if target[targetIndex] == -1:
                target[targetIndex] = targetNum
                continue
            else:
                target = target[:targetIndex] + [targetNum] + target[targetIndex:]
        
        return target[:len(nums)]
