class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        length = len(words)
        sortedSentence = [""] * length
        sentence = ""
        
        for word in words:
            index = int(word[-1])
            sortedSentence[index-1] = word[0:len(word)-1]
        
        for i in range(len(sortedSentence)):
            currWord = sortedSentence[i]
            if i == 0:
                sentence = currWord
            else:
                sentence += " " + currWord
        return sentence
        