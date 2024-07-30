# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/
class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums.pop(0)]
        arr2 = [nums.pop(0)]

        for num in nums:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        
        return arr1 + arr2
