"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(node, depthCounter):
            newDepth = depthCounter + 1
            if len(node.children) == 0:
                depths.append(newDepth)
                return
            else:
                for i in node.children:
                    if i is not None:
                        dfs(i, newDepth)
        
        depths = []
        if root is None:
            return 0
        else:
            dfs(root, 0)
            depths.sort()
            return depths[-1]