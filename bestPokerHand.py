# https://leetcode.com/problems/best-poker-hand/description/
class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        rankMap, suitMap = {}, {}
        
        # Build maps that count the cards
        for i in range(len(ranks)):
            rank = ranks[i]
            suit = suits[i]
            if rank in rankMap:
                rankMap[rank] += 1
            else:
                rankMap[rank] = 1
            if suit in suitMap:
                suitMap[suit] += 1
            else:
                suitMap[suit] = 1
        
        # Determine the best hands in order
        if len(suitMap) == 1:
            return "Flush"
        else:
            isPair = False
            for rank in rankMap:
                if rankMap[rank] == 2:
                    isPair = True
                elif rankMap[rank] >= 3:
                    return "Three of a Kind"
        
            if isPair == True:
                return "Pair"
        return "High Card"
                

        