class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}
        for c in s:
            if c in sMap:
                sMap[c] += 1
            else:
                sMap[c] = 1
        
        for c in t:
            if c in tMap:
                tMap[c] += 1
            else:
                tMap[c] = 1
        
        return sMap == tMap
                