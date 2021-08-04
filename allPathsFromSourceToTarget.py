class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(graph) == 0:
            return []
        
        stack = [(0, [])]
        allValidPaths = []
        paths = []
        target = len(graph) - 1
        
        while stack:
            
            currIndex, currPath = stack.pop()
            currPath.append(currIndex)
            neighbours = graph[currIndex]
            
            if len(neighbours) == 0 or currIndex == target:
                paths.append(currPath)
            else:
                for i in neighbours:
                    stack.append((i, list(currPath)))
                    
        for path in paths:
            if path[-1] == target:
                allValidPaths.append(path)
        
        return allValidPaths
        