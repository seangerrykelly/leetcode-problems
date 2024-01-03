# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/description/
class Solution(object):
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr.pop()
        lower, greater = [], []
        for item in arr:
            if item <= pivot:
                lower.append(item)
            else:
                greater.append(item)
        return self.quickSort(lower) + [pivot] + self.quickSort(greater)

    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        hardestWorkerId = 0
        workMap = {}
        for i in range(len(logs)):
            prevLeaveTime = 0 if i == 0 else currLog[1]
            currLog = logs[i]
            workerId, currLeaveTime = currLog
            if currLeaveTime - prevLeaveTime not in workMap:
                workMap[currLeaveTime - prevLeaveTime] = [workerId]
            else:
                workMap[currLeaveTime - prevLeaveTime].append(workerId)
        longestTaskTime = self.quickSort(workMap.keys()).pop()
        hardestWorkers = self.quickSort(workMap[longestTaskTime])
        return hardestWorkers[0]
            