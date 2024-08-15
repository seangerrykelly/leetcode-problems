# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        arr = [None for i in range(len(pref))]
        for i in range(len(pref)):
            if i == 0:
                arr[i] = pref[i]
                continue
            arr[i] = pref[i] ^ pref[i-1]

        return arr