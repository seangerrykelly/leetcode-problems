# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        traversal = []

        def traverse(node):
            if node is not None:
                if len(node.children) == 0:
                    traversal.append(node.val)
                else:
                    for child in node.children:
                        traversal.append(traverse(child))
                    traversal.append(node.val)
        
        traverse(root)
        traversal = [x for x in traversal if x is not None]

        return traversal
                