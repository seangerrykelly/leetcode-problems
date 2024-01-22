# https://leetcode.com/problems/sort-characters-by-frequency/description/
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        letterToFrequencyMap = {}
        for letter in s:
            if letter not in letterToFrequencyMap:
                letterToFrequencyMap[letter] = 1
            else:
                letterToFrequencyMap[letter] += 1
        
        frequencyToLetterMap = {}
        for letter in letterToFrequencyMap:
            frequency = letterToFrequencyMap[letter]
            if frequency not in frequencyToLetterMap:
                frequencyToLetterMap[frequency] = [letter]
            else:
                frequencyToLetterMap[frequency].append(letter)
        
        frequencies = frequencyToLetterMap.keys()
        frequencies.sort(reverse=True)

        for i in range(len(frequencies)):
            currFreq = frequencies[i]
            for letter in frequencyToLetterMap[currFreq]:
                currString = letter * currFreq
                result += currString
        
        return result
