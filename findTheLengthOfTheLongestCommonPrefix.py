# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2024-09-24
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixMap = {}
        longestPrefixLength = 0

        for num in arr1:
            numStr = str(num)
            prefix = ''
            for i in range(len(numStr)):
                prefix += numStr[i]
                if prefix not in prefixMap:
                    prefixMap[prefix] = 1
        
        for num in arr2:
            numStr = str(num)
            prefix = ''
            for i in range(len(numStr)):
                prefix += numStr[i]
                if prefix in prefixMap and len(prefix) > longestPrefixLength:
                    longestPrefixLength = len(prefix)

        return longestPrefixLength
