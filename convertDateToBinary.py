# https://leetcode.com/problems/convert-date-to-binary/
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        binaryDate = ""
        dateParts = date.split('-')

        for i in range(len(dateParts)):
            segment = dateParts[i]
            binarySegment = bin(int(segment))[2:]
            binaryDate += binarySegment
            if i != len(dateParts) - 1:
                binaryDate += '-'
        
        return binaryDate
