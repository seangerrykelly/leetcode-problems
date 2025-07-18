# https://leetcode.com/problems/determine-if-two-events-have-conflict/description/
class Solution(object):
    def convertTimeToInt(self, eventTime):
        time = eventTime.split(':')
        hours = int(time[0])
        mins = int(time[1])
        totalTime = hours*60 + mins
        return totalTime

    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        firstTimeRange = [self.convertTimeToInt(event1[0]), self.convertTimeToInt(event1[1])]
        secondTimeRange = [self.convertTimeToInt(event2[0]), self.convertTimeToInt(event2[1])]
        
        for time in range(secondTimeRange[0], secondTimeRange[1] + 1):
            if time in range(firstTimeRange[0], firstTimeRange[1] + 1):
                return True
        
        return False
