# https://leetcode.com/problems/to-lower-case/description/
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            letter = s[i]
            asciiCode = ord(letter)
            # Check if uppercase letter
            if asciiCode >= 65 and asciiCode <= 90:
                lowercaseLetter = chr(asciiCode + 32)
                result += lowercaseLetter
            else:
                result += s[i]
        
        return result