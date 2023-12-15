# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
class Solution(object):
    def getSubarrayComboCount(self, length):
        subarrayComboCount = 0
        for i in range(length + 1):
            subarrayComboCount += i
        
        # The arrays with len(1) are already counted, so subtract it
        return subarrayComboCount - 1

    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarrayList = []
        currSubarray = []
        subarrayCount = 0

        for num in nums:
            if num == 0:
                subarrayList.append([num])
                if len(currSubarray) > 0:
                    currSubarray.append(num)
                else:
                    currSubarray.append(num)
                    subarrayList.append(currSubarray)
                    subarrayCount += 1
            else:
                currSubarray = []

        for array in subarrayList:
            subarrayCount += self.getSubarrayComboCount(len(array))

        return subarrayCount
        