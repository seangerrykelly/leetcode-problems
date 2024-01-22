# https://leetcode.com/problems/find-the-difference/description/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for letter in s:
            t = t.replace(letter, "", 1)
        return t