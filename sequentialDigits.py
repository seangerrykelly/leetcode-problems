# https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-05-08
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sequentialDigits = []

        def getLowestSeq(num):
            numStr = str(num)
            base = ""
            seq = 1
            for i in range(1, len(numStr) + 1):
                base += str(seq)
                seq += 1
            return int(base)
        
        def getNextSeq(num):
            numStr = str(num)
            nextSeq = ""
            for digit in numStr:
                nextSeq += str(int(digit) + 1)
            return int(nextSeq)
        
        base = low
        currSeq = getLowestSeq(base)
        while currSeq <= high:
            currPower = len(str(currSeq))
            if currSeq >= low and currSeq <= high:
                sequentialDigits.append(currSeq)
            currSeq = getNextSeq(currSeq)
            if len(str(currSeq)) > currPower:
                base *= 10
                currSeq = getLowestSeq(base)
        
        return sequentialDigits
            