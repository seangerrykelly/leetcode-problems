# https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-10
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        cardMap = {}
        for card in hand:
            if card not in cardMap:
                cardMap[card] = 1
            else:
                cardMap[card] += 1
        
        while len(cardMap) > 0:
            straightHand = []
            minimumCard = min(cardMap.keys())
            for i in range(groupSize):
                if minimumCard not in cardMap:
                    return False
                else:
                    straightHand.append(minimumCard)
                    cardMap[minimumCard] -= 1
                
                if cardMap[minimumCard] == 0:
                    del cardMap[minimumCard]
                minimumCard += 1
                
        return True    