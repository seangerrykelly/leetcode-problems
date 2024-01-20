# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/description/
class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """

        # First map tables to dish names and counts
        tables = {}
        dishNames = {}
        for order in orders:
            tableNum = int(order[1])
            dish = order[2]
            if tableNum not in tables:
                tables[tableNum] = {}
            if dish not in tables[tableNum]:
                tables[tableNum][dish] = 1
                if dish not in dishNames:
                    dishNames[dish] = True
            else:
                tables[tableNum][dish] += 1
        
        # Sort the table numbers and the dish names
        sortedTableNums = tables.keys()
        sortedDishNames = dishNames.keys()
        sortedDishNames.sort()
        sortedTableNums.sort()

        # Build the table to be displayed
        displayTable = []
        displayTable.append(["Table"] + sortedDishNames)

        for tableNum in sortedTableNums:
            table = tables[tableNum]
            tableOrder = [str(tableNum)]
            for dishName in sortedDishNames:
                if dishName not in table:
                    tableOrder.append("0")
                else:
                    tableOrder.append(str(table[dishName]))
            displayTable.append(tableOrder)
        return displayTable
