# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        finalValue = 0
        for operation in operations:
            if operation[0] == '-' or operation[-1] == '-':
                finalValue -= 1
            else:
                finalValue += 1
        return finalValue