# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=daily-question&envId=2024-09-02
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        if len(chalk) == 1:
            return 0

        chalkSum = sum(chalk)
        while k >= chalkSum:
            k -= chalkSum
        
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        