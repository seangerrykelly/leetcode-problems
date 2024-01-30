# https://leetcode.com/problems/maximum-number-of-balloons/description/
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon = 'balloon'
        balloonMap = {}
        balloonCount = 0

        for letter in text:
            if letter not in balloonMap:
                balloonMap[letter] = 1
            else:
                balloonMap[letter] += 1
        
        tempBalloon = ""
        while True:
            for letter in balloon:
                if letter in balloonMap:
                    tempBalloon += letter
                    balloonMap[letter] -= 1
                    if balloonMap[letter] == 0:
                        del balloonMap[letter]
                else:
                    return balloonCount
                if tempBalloon == balloon:
                    balloonCount += 1
                    tempBalloon = ""
        return balloonCount
                