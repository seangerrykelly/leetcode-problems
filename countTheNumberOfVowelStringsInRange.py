# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = 'aeiou'
        vowelMap = {vowels[i]: True for i in range(len(vowels))}
        count = 0

        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowelMap and word[-1] in vowelMap:
                count += 1
        
        return count
