# https://leetcode.com/problems/number-of-recent-calls/description/
class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        requestRange = [t - 3000, t]
        result = 0
        self.requests.append(t)
        i = len(self.requests) - 1
        
        while i >= 0:
            request = self.requests[i]
            i -= 1
            if request >= requestRange[0] and request <= requestRange[1]:
                result += 1
            else:
                break

        return result

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)