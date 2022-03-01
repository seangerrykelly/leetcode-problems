class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = []
        for c in s:
            if c.isalpha() == True:
                letters.append(c.lower())
            elif c.isdigit() == True:
                letters.append(c)
        left, right = 0, len(letters) - 1
        
        while left <= right:
            if letters[left] != letters[right]:
                return False
            left += 1
            right -= 1
        
        return True