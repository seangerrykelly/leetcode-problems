# https://leetcode.com/problems/alphabet-board-path/description/
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        letterMap = {}
        currPosition = (0, 0)
        path = ""

        for i in range(len(board)):
            for j in range(len(board[i])):
                letterMap[board[i][j]] = (i, j)
        
        stack = []
        for letter in target:
            horizontal, vertical = letterMap[letter]
            if currPosition[0] - horizontal > 0:
                path += "U"*abs(currPosition[0] - horizontal)
            elif currPosition[0] - horizontal < 0:
                path += "D"*abs(currPosition[0] - horizontal)
            
            if vertical == 0 and horizontal == len(board) - 1 and currPosition[1] > 0:
                path = path[0:len(path)-1]
                stack.append("D")

            if currPosition[1] - vertical > 0:
                path += "L"*abs(currPosition[1] - vertical)
            elif currPosition[1] - vertical < 0:
                path += "R"*abs(currPosition[1] - vertical)
            
            if stack:
                path += stack.pop()

            path += "!"
            currPosition = (horizontal, vertical)
        
        return path
