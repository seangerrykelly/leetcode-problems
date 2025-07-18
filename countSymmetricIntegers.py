# https://leetcode.com/problems/count-symmetric-integers/
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0

        for i in range(low, high + 1):
            curr = str(i)
            if len(curr) % 2 != 0:
                continue
            first = curr[0:len(curr)/2]
            last = curr[len(curr)/2:]
            firstSum, lastSum = 0, 0
            for i in range(len(first)):
                firstSum += int(first[i])
                lastSum += int(last[i])
            if firstSum == lastSum:
                count += 1
        
        return count