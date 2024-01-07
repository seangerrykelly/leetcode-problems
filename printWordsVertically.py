# https://leetcode.com/problems/print-words-vertically/description/
class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = []
        currWord = ''
        maxWordLength = 0

        # Get all of the words with spaces included
        for i in range(len(s)):
            c = s[i]
            currWord += c
            if c == ' ' or i == len(s) - 1:
                words.append(currWord)
                if len(currWord) > maxWordLength:
                    maxWordLength = len(currWord)
                currWord = ''

        # Iterate through words and build verticalWords array
        verticalWords = []
        for word in words:
            for i in range(maxWordLength):
                character = ' ' if i > len(word) - 1 else word[i]
                if len(verticalWords) < i + 1:
                    verticalWords.append('')
                verticalWords[i] += character
        
        # Cleanup output
        result = []
        for word in verticalWords:
            word = word.rstrip()
            if word.isspace() or word == '':
                continue
            else:
                result.append(word)

        return result
                