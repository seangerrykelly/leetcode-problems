# https://leetcode.com/problems/number-complement/description/?envType=daily-question&envId=2024-08-22
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binaryNum = bin(num)[2:]
        complement = 0
        currPower = 0
        for i in reversed(range(len(binaryNum))):
            if binaryNum[i] == '0':
                complement += 2**currPower
            currPower += 1
        
        return complement