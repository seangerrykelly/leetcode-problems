# https://leetcode.com/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2024-04-24
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        goodInts = []
        numString = str(num)
        for i in range(0, len(numString)-2):
            curr = numString[i:i+3]
            if all(num == numString[i] for num in curr):
                goodInts.append(int(curr))
        
        if len(goodInts) > 0:
            maxInt = max(goodInts)
            if maxInt == 0:
                return "0" * 3
            return str(maxInt)
        return ""