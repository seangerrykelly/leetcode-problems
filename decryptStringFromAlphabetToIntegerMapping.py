# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabetMap = {str(i+1):alphabet[i] for i in range(len(alphabet))}
        decryptedString = ""
        i = 0
        
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == '#':
                substring = s[i:i+2]
                i += 3
            else:
                substring = s[i]
                i += 1
            decryptedString += alphabetMap[substring]
        
        return decryptedString