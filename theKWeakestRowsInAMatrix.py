# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        weakestRows = []

        # Map the soldier count to an array of indices
        soldierMap = {}
        for i in range(len(mat)):
            soldiers = []
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    soldiers.append(mat[i][j])
                else:
                    break
            if len(soldiers) not in soldierMap:
                soldierMap[len(soldiers)] = [i]
            else:
                soldierMap[len(soldiers)].append(i)
        
        # Go through soldierMap keys in order
        soldierKeys = soldierMap.keys()
        soldierKeys.sort()

        for i in range(len(soldierKeys)):
            currKey = soldierKeys[i]
            for j in range(len(soldierMap[currKey])):
                weakestRows.append(soldierMap[currKey][j])
                if len(weakestRows) == k:
                    return weakestRows

        return weakestRows