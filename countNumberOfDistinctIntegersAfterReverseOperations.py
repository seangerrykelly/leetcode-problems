# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/
class Solution(object):
    def reverseInt(self, num):
        numString = str(num)
        reverseNum = 0
        i = len(numString) - 1
        while i >= 0:
            power = numString[i]
            reverseNum += int(power) * 10**i
            i -= 1
        return reverseNum


    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinctIntMap = {}
        numsLength = len(nums)

        def updateIntMap(num):
            if num not in distinctIntMap:
                distinctIntMap[num] = 1

        for i in range(numsLength):
            num = nums[i]
            updateIntMap(num)
            reverseNum = self.reverseInt(num)
            nums.append(reverseNum)
            updateIntMap(reverseNum)

        return len(distinctIntMap)
            