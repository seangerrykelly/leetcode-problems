# https://leetcode.com/problems/adding-spaces-to-a-string/description/
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        if len(spaces) == 0:
            return s

        # Need to use a string list and then .join to avoid Time Limit Exceeded error
        currSpace = 0
        stringList = []

        for i in range(len(s)):
            if currSpace < len(spaces) and i == spaces[currSpace]:
                stringList.append(" ")
                currSpace += 1
            stringList.append(s[i])
        
        return "".join(stringList)
        