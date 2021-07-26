# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        
        def dfs(node1, node2, prevNode, isLeft):
            
            if node1 is None and node2 is None or node2 is None:
                return
            
            if node1 is None:
                if isLeft is True:
                    prevNode.left = node2
                else:
                    prevNode.right = node2
                return
            node1.val += node2.val
            prevNode = node1
            dfs(node1.left, node2.left, prevNode, True)
            dfs(node1.right, node2.right, prevNode, False)
            
        dfs(root1, root2, None, False)
        return root1