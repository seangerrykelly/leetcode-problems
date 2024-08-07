# https://leetcode.com/problems/a-number-after-a-double-reversal/description/
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])
        return num == reversed2
        