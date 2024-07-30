# https://leetcode.com/problems/number-of-senior-citizens/description/
class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        seniorCount = 0
        for passenger in details:
            age = passenger[11:13]
            if int(age) > 60:
                seniorCount += 1
        return seniorCount