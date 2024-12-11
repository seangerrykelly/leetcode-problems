# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/
class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        letterStack = []

        for i in range(len(s)):
            letterStack.append(s[i])
            if len(letterStack) >= len(part):
                substring = "".join(letterStack[len(letterStack)-len(part):])
                if substring == part:
                    for i in range(len(part)):
                        letterStack.pop()
        
        return "".join(letterStack)