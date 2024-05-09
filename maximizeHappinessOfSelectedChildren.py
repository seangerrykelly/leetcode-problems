# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        maxHappiness = 0
        currTurn = 0
        happiness.sort()

        while currTurn < k:
            child = happiness.pop() - currTurn
            if child < 0:
                child = 0
            maxHappiness += child
            currTurn += 1
        
        return maxHappiness