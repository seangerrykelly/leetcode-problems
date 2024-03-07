# https://leetcode.com/problems/minimum-number-game/description/
class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arr = []
        
        alice, bob = 0, 1
        while bob < len(nums):
            currAlice, currBob = nums[alice], nums[bob]
            arr.append(currBob)
            arr.append(currAlice)
            alice += 2
            bob += 2

        return arr