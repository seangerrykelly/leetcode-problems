# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11
class Solution(object):
    def quickSort(self, sortMap, characters):
        if len(characters) <= 1:
            return characters
        
        pivot = characters.pop()
        lower, greater = [], []

        for c in characters:
            if sortMap[c] <= sortMap[pivot]:
                lower.append(c)
            else:
                greater.append(c)
        
        return self.quickSort(sortMap, lower) + [pivot] + self.quickSort(sortMap, greater)

    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        orderMap = {}
        index = 0
        for letter in order:
            orderMap[letter] = index
            index += 1
        
        for letter in s:
            # letters not defined in order string can appear in any order
            if letter not in orderMap:
                orderMap[letter] = 0
        
        letters = [x for x in s]

        # Sort an array of characters based on order given
        sortedLetters = self.quickSort(orderMap, letters)
        result = ""

        # Build result from sorted array
        for letter in sortedLetters:
            result += letter

        return result



        
        