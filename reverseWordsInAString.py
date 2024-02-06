# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        s = ""
        for i in reversed(range(len(words))):
            if i == 0:
                s += words[i]
            else:
                s += words[i] + ' '
        return s
        