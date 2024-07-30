# https://leetcode.com/problems/keyboard-row/description/
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        answer = []
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        keyboardMap = {}

        for i in range(len(rows)):
            row = rows[i]
            for letter in row:
                keyboardMap[letter] = i

        for word in words:
            currRow = None
            isOneRow = True
            for i in range(len(word)):
                letter = word[i].lower()
                if i == 0:
                    currRow = keyboardMap[letter]
                elif keyboardMap[letter] != currRow:
                    isOneRow = False
                    break
            if isOneRow:
                answer.append(word)
                
        return answer