# https://leetcode.com/problems/number-of-changing-keys/description/
class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        keyChanges = 0
        prev, curr = None, None
        for i in range(len(s)):
            if i == 0:
                prev = s[i].lower()
                continue
            curr = s[i].lower()
            if curr != prev:
                keyChanges += 1
            prev = curr

        return keyChanges
        