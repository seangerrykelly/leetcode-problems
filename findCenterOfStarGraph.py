# https://leetcode.com/problems/find-center-of-star-graph/description/?envType=daily-question&envId=2024-06-27
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        nodeMap = {}
        for edge in edges:
            startNode, endNode = edge
            if startNode not in nodeMap:
                nodeMap[startNode] = True
            else:
                return startNode
            if endNode not in nodeMap:
                nodeMap[endNode] = True
            else:
                return endNode