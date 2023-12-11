# https://leetcode.com/problems/decode-the-message/submissions/
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decodedMessage = ""
        cypher = {' ': ' '}
        alphabetIndex = 0
        for letter in key:
            if letter not in cypher and letter.isalpha():
                cypher[letter] = alphabet[alphabetIndex]
                alphabetIndex += 1
        
        for letter in message:
            decodedMessage += cypher[letter]
            
        return decodedMessage