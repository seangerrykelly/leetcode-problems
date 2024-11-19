# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/
class Solution(object):
    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        leftDist, rightDist = 0, 0
        counter = 0
        currIndex = startIndex

        if target not in words:
            return -1

        while counter < len(words):
            curr = words[currIndex]
            if curr == target:
                break
            if currIndex - 1 < 0:
                currIndex = len(words)
            leftDist += 1
            currIndex -= 1
            counter += 1
        
        currIndex = startIndex
        counter = 0
        while counter < len(words):
            curr = words[currIndex]
            if curr == target:
                break
            if currIndex + 1 >= len(words):
                currIndex = -1
            rightDist += 1
            currIndex += 1
            counter += 1
        
        return min(leftDist, rightDist)