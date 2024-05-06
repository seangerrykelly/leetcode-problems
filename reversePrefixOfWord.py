# https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=daily-question&envId=2024-05-01
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        for i in range(len(word)):
            letter = word[i]
            if word[i] == ch:
                word = word[0:i+1][::-1] + word[i+1:]
                break
        
        return word