# https://leetcode.com/problems/time-needed-to-buy-tickets/description/
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        timeRequired = 0
        currIndex = 0
        while tickets[k] != 0:
            currPerson = tickets[currIndex]
            if currPerson > 0:
                timeRequired += 1
                tickets[currIndex] -= 1
            currIndex += 1

            if currIndex == len(tickets):
                currIndex = 0
        return timeRequired
            
