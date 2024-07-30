class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        bracketStack = []
        bracketCount = 0
        words = []
        currWord = 0
        reversedWord = ""

        for letter in s:
            if letter == '(':
                bracketStack.append(letter)
                bracketCount += 1
                words.append("")
                currWord = len(words) - 1
            elif letter == ')':
                bracketStack.pop()
                bracketCount += 1
                curr = words.pop(currWord)[::-1]
                currWord -= 1
                if len(words) != 0:
                    words[currWord] += curr
                else:
                    reversedWord += curr
            elif len(bracketStack) > 0:
                words[currWord] += letter
            else:
                reversedWord += letter
                
        return reversedWord