# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleIndex = -1

        if len(needle) > len(haystack):
            return needleIndex
        
        maxIterations = len(haystack) - len(needle) + 1

        for i in range(maxIterations):
            potentialNeedle = haystack[i:i + len(needle)]
            if potentialNeedle == needle:
                needleIndex = i
                break
        return needleIndex
        
        