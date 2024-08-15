# https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnNumber = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabetMap = {alphabet[i]: i+1 for i in range(len(alphabet))}
        currMultiplier = 0

        for i in reversed(range(len(columnTitle))):
            columnNumber += (26**currMultiplier)*alphabetMap[columnTitle[i].lower()]
            currMultiplier += 1
        
        return columnNumber
