# https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01
class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 1

        for i in range(len(word)):
            if i == 0:
                continue
            prev, curr = word[i-1], word[i]
            if prev == curr:
                count += 1
        
        return count
        