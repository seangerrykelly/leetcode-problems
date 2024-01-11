# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        C = []
        n = len(A) # len(A) == len(B) in the problem description
        AMap, BMap = {}, {}
        commonCount = 0

        for i in range(n):
            currA, currB = A[i], B[i]
            if currA not in AMap: 
                AMap[currA] = 1
            if currB not in BMap:
                BMap[currB] = 1
            
            if currA == currB:
                commonCount += 1
            else:
                if currB in AMap:
                    commonCount += 1
                if currA in BMap:
                    commonCount += 1
            C.append(commonCount)
        return C