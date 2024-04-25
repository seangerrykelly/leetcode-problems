# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=daily-question&envId=2024-04-24
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tribArr = [0 for i in range(38)]
        tribArr[0], tribArr[1], tribArr[2] = 0, 1, 1

        for i in range(3, len(tribArr)):
            currTrib = tribArr[i-3] + tribArr[i-2] + tribArr[i-1]
            tribArr[i] = currTrib

        return tribArr[n]