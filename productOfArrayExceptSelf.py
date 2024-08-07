# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        prefix, suffix = 'prefix', 'suffix'
        productMap = {}
        currPrefix, currSuffix = 1, 1
        for i in range(len(nums)):
            productMap[i] = {prefix: 1, suffix: 1}
            if i == 0:
                continue
            currPrefix *= nums[i-1]
            productMap[i][prefix] = currPrefix
        
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue
            currSuffix *= nums[i+1]
            productMap[i][suffix] = currSuffix
        
        for i in range(len(nums)):
            productExceptSelf = productMap[i][prefix] * productMap[i][suffix]
            answer.append(productExceptSelf)

        return answer
                    