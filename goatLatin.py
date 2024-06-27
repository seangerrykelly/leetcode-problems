# https://leetcode.com/problems/goat-latin/description/
class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        vowelMap = {}
        for vowel in vowels:
            vowelMap[vowel] = 1
        
        words = sentence.split()
        for i in range(len(words)):
            word = words[i]
            wordIndex = i + 1
            if word[0] not in vowelMap:
                firstLetter = word[0]
                word = word[1:] + firstLetter + 'ma' + ('a'*wordIndex)
            else:
                word = word + 'ma' + ('a'*wordIndex)
            words[i] = word
        
        return " ".join(words)
