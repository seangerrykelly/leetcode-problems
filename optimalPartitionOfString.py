# https://leetcode.com/problems/optimal-partition-of-string/description/
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        partitions = []
        letterMap = {}

        currPartition = ""
        for i in range(len(s)):
            letter = s[i]
            if letter not in letterMap:
                letterMap[letter] = 1
                currPartition += letter
            else:
                partitions.append(currPartition)
                letterMap = {letter: 1}
                currPartition = letter
            
            if i == len(s) - 1:
                # final iteration
                partitions.append(currPartition)
        
        return len(partitions)