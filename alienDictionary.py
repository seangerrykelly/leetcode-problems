class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        isAlienSorted = False
        alienDictionary = {}
        for i in range(len(order)):
            alienDictionary[order[i]] = i
        
        for i in range(len(words) - 1):
            firstWord = words[i]
            for j in range(i + 1, len(words)):
                secondWord = words[j]
                isValid = False
                minLength = min(len(firstWord), len(secondWord))
                for k in range(minLength):
                    if alienDictionary[firstWord[k]] < alienDictionary[secondWord[k]] or firstWord == secondWord:
                        isValid = True
                        break
                    elif alienDictionary[firstWord[k]] == alienDictionary[secondWord[k]]:
                        if k == minLength - 1:
                            if len(firstWord) < len(secondWord):
                                isValid = True
                                break
                        continue
                    else:
                        return False
                    
                        
                if isValid == False:
                    return isValid
                isAlienSorted = isValid
            
        return isAlienSorted