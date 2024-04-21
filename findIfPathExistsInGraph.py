# https://leetcode.com/problems/find-if-path-exists-in-graph/description/?envType=daily-question&envId=2024-04-21
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        pathMap = {destination: {}}

        # Build map of paths. Remember it is bi-directional
        for i in range(len(edges)):
            start, end = edges[i]
            if start not in pathMap:
                pathMap[start] = { end: True }
            else:
                pathMap[start][end] = True
            if end not in pathMap:
                pathMap[end] = { start: True }
            else:
                pathMap[end][start] = True
                
        # Now do depth-first search of the graph using pathMap
        stack = [source]
        checkedNodes = {}

        while stack:
            currNode = stack.pop()
            checkedNodes[currNode] = 1

            for node in pathMap[currNode]:
                if node == destination:
                    return True
                elif node not in checkedNodes:
                    stack.append(node)

        return False