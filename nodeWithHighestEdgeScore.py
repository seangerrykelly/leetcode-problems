class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        edgeToScoreMap = {i: 0 for i in range(len(edges))}
        scoreToEdgeMap = {}

        for i in range(len(edges)):
            currNode = i
            endNode = edges[i]
            edgeToScoreMap[endNode] += currNode
        
        for edge in edgeToScoreMap:
            score = edgeToScoreMap[edge]
            if score not in scoreToEdgeMap:
                scoreToEdgeMap[score] = [edge]
            else:
                scoreToEdgeMap[score].append(edge)
        
        scores = scoreToEdgeMap.keys()
        maxScoreEdges = scoreToEdgeMap[max(scores)]
        
        return min(maxScoreEdges)
