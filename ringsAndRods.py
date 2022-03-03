class Solution:
    def countPoints(self, rings: str) -> int:
        ringColourMap = {}
        ringCount = 0
        prev = None
        for character in rings:
            
            if prev == None:
                prev = character
                continue
                
            if character.isdigit():
                if character in ringColourMap and prev in ringColourMap[character]:
                    ringColourMap[character][prev] += 1
                elif character not in ringColourMap:
                    ringColourMap[character] = {prev: 1}
                elif character in ringColourMap and prev not in ringColourMap[character]:
                    ringColourMap[character][prev] = 1
                    
            elif character.isalpha():
                prev = character
        
        for key in ringColourMap:
            if len(ringColourMap[key]) == 3:
                ringCount += 1
        return ringCount