# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in diffMap:
                diffMap[curr] = [i]
            else:
                diffMap[curr].append(i)
                
        for diff in diffMap:
            targetDiff = target - diff
            if targetDiff in diffMap:
                if targetDiff != diff:
                    return [diffMap[diff].pop(), diffMap[targetDiff].pop()]
                elif targetDiff == diff and len(diffMap[diff]) > 1:
                    return diffMap[diff]
                else:
                    continue

