# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        levelOrderTraversal = []

        def traverse(node, level):
            if node is not None:
                if len(levelOrderTraversal) < level:
                    levelOrderTraversal.append([])
                levelOrderTraversal[level-1].append(node.val)
                for child in node.children:
                    traverse(child, level + 1)
        traverse(root, 1)
        return levelOrderTraversal
        