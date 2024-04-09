# https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-04-07
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Map the maps of each word to an array 
        anagrams = {}

        # Build map of anagrams by sorting chars in each string
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = [word]
            else:
                anagrams[sortedWord].append(word)

        # Return the array of arrays stored in the map
        return anagrams.values()
