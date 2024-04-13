# https://leetcode.com/problems/number-of-different-integers-in-a-string/description/
class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        intMap = {}
        intString = ""

        for i in word:
            if i.isdigit():
                intString += i
            elif len(intString) > 0:
                num = int(intString)
                intMap[num] = 1
                intString = ""
        
        if len(intString) > 0:
            num = int(intString)
            intMap[num] = 1
        
        return len(intMap)
            