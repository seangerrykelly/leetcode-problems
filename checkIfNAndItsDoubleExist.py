# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        intMap = {}
        for num in arr:
            if num not in intMap:
                intMap[num] = 1
            else:
                intMap[num] += 1

        for num in arr:
            double = num * 2
            if double != 0 and double in intMap:
                return True
            elif double == 0 and double in intMap:
                if intMap[double] > 1:
                    return True
        return False        