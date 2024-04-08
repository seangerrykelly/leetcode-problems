# https://leetcode.com/problems/sum-multiples/description/
class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        divisors = [3,5,7]
        sumOfMultiples = 0

        for i in range(1, n + 1):
            for divisor in divisors:
                if i % divisor == 0:
                    sumOfMultiples += i
                    break
        
        return sumOfMultiples