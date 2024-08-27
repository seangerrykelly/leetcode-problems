# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(words) != len(s):
            return False
        
        for i in range(len(words)):
            if s[i] != words[i][0]:
                return False
        
        return True