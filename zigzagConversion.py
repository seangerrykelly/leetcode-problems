# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        # First build the 2D Array
        wordMatrix = [[] for i in range(numRows)]
        inbetweenColCount = numRows - 2
        wordIter = iter(s)
        charCount = len(s)
        isFullColumn = True
        while charCount > 0:
            if isFullColumn:
                for i in range(numRows):
                    if charCount == 0:
                        break
                    wordMatrix[i].append(wordIter.next())
                    charCount -= 1
                isFullColumn = False
            else:
                while inbetweenColCount > 0:
                    if charCount == 0:
                        break
                    wordMatrix[inbetweenColCount].append(wordIter.next())
                    charCount -= 1
                    inbetweenColCount -= 1
                inbetweenColCount = numRows - 2
                isFullColumn = True
        
        # Then build the output string using the 2D Array
        result = ""
        for word in wordMatrix:
            for character in word:
                if character != '':
                    result += character

        return result