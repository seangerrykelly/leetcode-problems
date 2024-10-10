# https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2024-10-08
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = [str(i) for i in range(1, n + 1)]
        nums.sort()
        nums = [int(nums[i]) for i in range(len(nums))]
        return nums