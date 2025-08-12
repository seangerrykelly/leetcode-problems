# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        groups = []

        while len(s) > 0:
            group = s[:k]
            s = s[k:]
            if len(group) < k:
                group += fill * (k - len(group))

            groups.append(group)

        return groups