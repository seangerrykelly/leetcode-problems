# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        
        return " ".join(words)