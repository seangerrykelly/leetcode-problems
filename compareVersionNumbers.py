# https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2024-08-14
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        order = 0
        arr1, arr2 = version1.split('.'), version2.split('.')
        if len(arr1) < len(arr2):
            arr1 += '0' * (len(arr2)-len(arr1))
        elif len(arr2) < len(arr1):
            arr2 += '0' * (len(arr1)-len(arr2))

        # both arrays are of equal size now so we can compare each element
        for i in range(len(arr1)):
            v1, v2 = int(arr1[i]), int(arr2[i])
            if v1 > v2:
                order = 1
                break
            elif v1 < v2:
                order = -1
                break

        return order