# https://leetcode.com/problems/rearrange-spaces-between-words/description/
class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaceCount = 0
        words = text.split()
        for letter in text:
            if letter == ' ':
                spaceCount += 1
        
        if len(words) == 1:
            return words[0] + ' '*spaceCount
        
        spacesPerWord = spaceCount / (len(words) - 1)
        extraSpaces = spaceCount - spacesPerWord*(len(words) - 1)

        result = ''
        for i in range(len(words)):
            word = words[i]
            if i < len(words) - 1:
                word += ' ' * spacesPerWord
            else:
                word += ' ' * extraSpaces
            result += word
        
        return result