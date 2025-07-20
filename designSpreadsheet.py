# https://leetcode.com/problems/design-spreadsheet/description/
import re

class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.cellMap = {}
        for i in range(len(alphabet)):
            for j in range(1, rows + 1):
                cell = alphabet[i] + str(j)
                self.cellMap[cell] = 0

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.cellMap[cell] = value
        
    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.cellMap[cell] = 0

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # Parse formula for cell coords or integers
        cells = re.split(r'[+=]', formula)
        cells.pop(0)
        firstVal, secondVal = cells

        def getFormulaValue(val):
            if val not in self.cellMap:
                return int(val)
            else:
                return self.cellMap[val]
        
        return getFormulaValue(firstVal) + getFormulaValue(secondVal)
        
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)