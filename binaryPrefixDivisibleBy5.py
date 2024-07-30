# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        prefixSum = ""
        answer = []

        for i in range(len(nums)):
            prefixSum += str(nums[i])
            baseTenNum = int(prefixSum, 2)
            if baseTenNum % 5 == 0:
                answer.append(True)
            else:
                answer.append(False)

        return answer