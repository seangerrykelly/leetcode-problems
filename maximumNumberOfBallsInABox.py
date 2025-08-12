# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {}
        maximumBox = None

        for num in range(lowLimit, highLimit + 1):
            # Get sum of all digits
            boxLabel = str(num)
            ballSum = 0
            for digit in boxLabel:
                ballSum += int(digit)

            if ballSum not in boxes:
                boxes[ballSum] = 1
            else:
                boxes[ballSum] += 1
            
            if maximumBox == None or boxes[ballSum] > boxes[maximumBox]:
                maximumBox = ballSum
        
        return boxes[maximumBox]
