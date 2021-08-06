class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniqueMorseCount = 0
        morseAlphabetMap = {}
        morseWordMap = {}
        
        for i in range(len(alphabet)):
            morseAlphabetMap[alphabet[i]] = morseAlphabet[i]
        
        for word in words:
            morseWord = ""
            for character in word:
                morseWord = morseWord + morseAlphabetMap[character]
            
            if morseWordMap.get(morseWord) is None:
                uniqueMorseCount += 1
                morseWordMap[morseWord] = True 
        
        return uniqueMorseCount