# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        subRootTraversal = []
        candidates = []
        def dfs(node, isSubRoot):
            if node is None:
                if isSubRoot:
                    subRootTraversal.append(None)
                return
            if isSubRoot:
                subRootTraversal.append(node.val)
            elif node.val == subRoot.val:
                candidates.append(node)
            dfs(node.left, isSubRoot)
            dfs(node.right, isSubRoot)

        dfs(subRoot, True)
        dfs(root, False)
        subRootTraversalClone = subRootTraversal[:]

        for node in candidates:
            subRootTraversal = []
            dfs(node, True)
            if subRootTraversal == subRootTraversalClone:
                return True


        return False
        