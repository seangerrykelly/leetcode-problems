class Solution(object):
    def updateMapAndCheckStillValid(self, cellMap, cell):
        if cell not in cellMap and cell.isdigit():
            cellMap[cell] = 1
            return True
        elif cell in cellMap:
            return False
        return True
            

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check if the input is valid before anything else
        if len(board) != 9:
            return False
        else:
            for row in board:
                if len(row) != 9:
                    return False
        
        # Then iterate through the board, keeping track of rows, columns, and sub-boxes
        rows, cols, boxes = [{} for x in range(9)], [{} for x in range(9)], [{} for x in range(9)]
        rowCounter, colCounter, boxCounter = 0, 0, 0

        for row in board:
            if rowCounter % 3 == 0 and rowCounter != 0:
                # Every 3 rows, increment boxCounter by 3
                boxCounter += 3          
            for cell in row:
                if colCounter % 3 == 0 and colCounter != 0:
                    # Every 3 cols, increment boxCounter by 1
                    boxCounter += 1
                
                updatedRow = self.updateMapAndCheckStillValid(rows[rowCounter], cell)
                updatedCol = self.updateMapAndCheckStillValid(cols[colCounter], cell)
                updatedBox = self.updateMapAndCheckStillValid(boxes[boxCounter], cell)

                if updatedRow == False or updatedCol == False or updatedBox == False:
                    return False                
                
                colCounter += 1
            rowCounter += 1
            colCounter = 0
            boxCounter -= 2 # When cols = 0 again, subtract boxCounter by 2
        return True