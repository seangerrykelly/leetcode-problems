class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterMap = {}
        for letter in magazine:
            if letter not in letterMap:
                letterMap[letter] = 1
            else:
                letterMap[letter] += 1
        
        for letter in ransomNote:
            if letter in letterMap and letterMap[letter] > 0:
                letterMap[letter] -= 1
            else:
                return False
        
        return True