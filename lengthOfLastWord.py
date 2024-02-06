# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
# This one is way too easy
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])