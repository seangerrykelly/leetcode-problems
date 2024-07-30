# https://leetcode.com/problems/pass-the-pillow/?envType=daily-question&envId=2024-07-06
class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        curr = 1
        isForward = True

        while time > 0:
            time -= 1
            if isForward:
                curr += 1
                if curr == n:
                    isForward = False
            else:
                curr -= 1
                if curr == 1:
                    isForward = True
        
        return curr
            

        