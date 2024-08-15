# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        stepCount = 0

        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            stepCount += 1
        
        return stepCount
        