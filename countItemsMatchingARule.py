# https://leetcode.com/problems/count-items-matching-a-rule/description/
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        ruleMap = {'type': 0, 'color': 1, 'name': 2}
        ruleIndex = ruleMap[ruleKey]
        matchCount = 0

        for item in items:
            if item[ruleIndex] == ruleValue:
                matchCount += 1
        
        return matchCount
