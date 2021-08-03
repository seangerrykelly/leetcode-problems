class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        charArray = [''] * len(s)
        currIndex = 0
        for i in indices:
            charArray[i] = s[currIndex]
            currIndex += 1
        restoredString = "".join(charArray)
        return restoredString