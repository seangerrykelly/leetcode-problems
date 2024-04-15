# https://leetcode.com/problems/is-subsequence/submissions/1232602032/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        isSubsequence = False
        sIndex = 0

        if len(s) == 0:
            return True

        for i in t:
            if i == s[sIndex]:
                sIndex += 1
            
            if sIndex > len(s) - 1:
                isSubsequence = True
                break
        
        return isSubsequence
            