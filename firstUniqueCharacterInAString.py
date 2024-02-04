# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        characterMap = {}
        result = -1

        # Create a map of all of the characters
        for letter in s:
            if letter not in characterMap:
                characterMap[letter] = 1
            else:
                characterMap[letter] += 1

        # Go through the string again and check the map
        for i in range(len(s)):
            curr = s[i]
            if characterMap[curr] == 1:
                result = i
                break
        
        return result
        
        