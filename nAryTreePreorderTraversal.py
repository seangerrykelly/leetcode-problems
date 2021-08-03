"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        preorderTraversal = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr is None:
                continue
            i = len(curr.children) - 1
            while i >= 0:
                stack.append(curr.children[i])
                i -= 1
            preorderTraversal.append(curr.val)
        return preorderTraversal