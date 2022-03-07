class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userActivityMap = {}
        activeMinutesMap = {}
        result = [0] * k
        
        for pair in logs:
            userId, currMinute = pair
            if userId not in userActivityMap:
                userActivityMap[userId] = {currMinute: True}
            elif currMinute not in userActivityMap[userId]:
                userActivityMap[userId][currMinute] = True
        
        for key in userActivityMap:
            currUser = userActivityMap[key]
            activeMinutes = len(currUser)
            if activeMinutes in activeMinutesMap:
                activeMinutesMap[activeMinutes] += 1
            else:
                activeMinutesMap[activeMinutes] = 1
        
        for i in range(len(result)):
            currMinute = i + 1
            if currMinute in activeMinutesMap:
                result[i] = activeMinutesMap[currMinute]

        return result
                