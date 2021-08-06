class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        letterMap = {}
        
        for letter in alphabet:
            letterMap[letter] = False
            
        for character in sentence:
            if letterMap.get(character) is not None:
                letterMap[character] = True
        
        if False in letterMap.values():
            return False
        else:
            return True