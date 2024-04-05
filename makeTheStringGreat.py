# https://leetcode.com/problems/make-the-string-great/description/?envType=daily-question&envId=2024-04-05
class Solution(object):
    def checkString (self, s):
        prev, curr = "", ""
        removeChars = []
        for i in range(len(s)):
            if i == 0:
                prev = i
            else:
                curr = i
                prevAscii = ord(s[prev])
                currAscii = ord(s[curr])

                if currAscii == prevAscii + 32 or currAscii == prevAscii - 32:
                    # If they're the same letter but different cases
                    removeChars.append(prev)
                    removeChars.append(curr)
                    break
                prev = curr
        return removeChars

    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        while True:
            removeChars = self.checkString(s)
            if len(removeChars) == 0:
                break
            else:
                s = s[:removeChars[0]] + s[removeChars[1] + 1:]
        removeChars = self.checkString(s)

        return s