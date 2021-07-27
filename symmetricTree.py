# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, node):
        if node is None:
            return
        else:
            leftCopy = node.left
            node.left = node.right
            node.right = leftCopy
            self.invertTree(node.left)
            self.invertTree(node.right)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        leftStack = [root.val]
        rightStack = [root.val]
        
        def dfs(node, stack):
            if node is None:
                stack.append(None)
                return
            else:
                stack.append(node.val)
                dfs(node.left, stack)
                dfs(node.right, stack)
        
        self.invertTree(root.left)
        dfs(root.left, leftStack)
        dfs(root.right, rightStack)
        
        return leftStack == rightStack