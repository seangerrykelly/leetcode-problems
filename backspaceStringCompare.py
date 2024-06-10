# https://leetcode.com/problems/backspace-string-compare/
class Solution(object):
    def interpretBackspaces(self, word):
        backspace = "#"
        currIndex = 0
        chars = list(word)

        while currIndex < len(chars):
            if currIndex < len(chars) - 1:
                nextChar = chars[currIndex + 1]
                if nextChar == backspace:
                    chars.pop(currIndex)
                    chars.pop(currIndex)
                    currIndex = 0
                    continue
            currIndex += 1
        chars = [x for x in chars if x != backspace]

        return "".join(chars)

    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = self.interpretBackspaces(s)
        t = self.interpretBackspaces(t)

        return s == t