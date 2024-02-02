# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = [i + 1 for i in range(n)]
        count = k
        i = 0
        
        while len(friends) > 1:
            currFriend = friends[i]
            count -= 1
            if count == 0:
                friends.pop(i)
                count = k
            else:
                i += 1

            if i == len(friends):
                i = 0

        return friends[0]