# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        distinctMap = {}

        # Build map of distinct strings
        for word in arr:
            if word not in distinctMap:
                distinctMap[word] = 1
            else:
                distinctMap[word] += 1
        
        currK = 1
        for word in arr:
            if distinctMap[word] == 1:
                if currK == k:
                    return word
                currK += 1                
        
        return ""
        