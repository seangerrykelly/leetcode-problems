class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowedChars = {}
        consistentStringCount = len(words)
        
        for character in allowed:
            allowedChars[character] = True
        
        for word in words:
            for character in word:
                if allowedChars.get(character) is None:
                    consistentStringCount -= 1
                    break
        
        return consistentStringCount