# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        for employee in hours:
            if employee >= target:
                result += 1
        return result