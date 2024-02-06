# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestPrefix = ""
        currPrefix = strs[0][0:1]
        currIndex = 0
        strs.sort()
        
        while currIndex < len(strs[0]):
            currPrefix = strs[0][0:currIndex + 1]
            isEqual = True
            for i in range(1, len(strs)):
                if currIndex < len(strs[i]):
                    if currPrefix == strs[i][0:currIndex + 1]:
                        continue
                    else:
                        isEqual = False
                else:
                    break
            if isEqual:
                longestPrefix = currPrefix
                currIndex += 1
            else:
                break
                
        return longestPrefix