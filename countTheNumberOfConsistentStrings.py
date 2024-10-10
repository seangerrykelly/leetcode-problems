# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowMap = {allowed[i]: True for i in range(len(allowed))}
        consistentCount = 0

        for word in words:
            isConsistent = True
            for letter in word:
                if letter not in allowMap:
                    isConsistent = False
                    break
            if isConsistent:
                consistentCount += 1
        
        return consistentCount