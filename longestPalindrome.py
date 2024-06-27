# https://leetcode.com/problems/longest-palindrome/description
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterMap = {}
        for letter in s:
            if letter not in letterMap:
                letterMap[letter] = 1
            else:
                letterMap[letter] += 1
        
        maxOddLetter = None
        evenCount = 0
        oddCount = 0

        for letter in letterMap:
            if letterMap[letter] % 2 == 0:
                evenCount += letterMap[letter]
            else:
                if maxOddLetter == None:
                    maxOddLetter = letter
                elif letterMap[letter] > letterMap[maxOddLetter]:
                    maxOddLetter = letter

        for letter in letterMap:
            if letterMap[letter] % 2 != 0 and letter != maxOddLetter:
                oddCount += letterMap[letter] - 1
            elif letter == maxOddLetter:
                oddCount += letterMap[letter]
        
        return oddCount + evenCount