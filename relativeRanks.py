# https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ranks = ["" for i in range(len(score))]
        scoreMap = {}
        sortedScores = score[:]
        sortedScores.sort(reverse=True)

        for i in range(len(sortedScores)):
            athlete = sortedScores[i]
            if i == 0:
                scoreMap[athlete] = "Gold Medal"
            elif i == 1:
                scoreMap[athlete] = "Silver Medal"
            elif i == 2:
                scoreMap[athlete] = "Bronze Medal"
            else:
                scoreMap[athlete] = str(i + 1)
        
        for i in range(len(score)):
            ranks[i] = scoreMap[score[i]]
        
        return ranks
        