# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(node):
            if node is None:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        values = []
        dfs(root)
        values.sort()
        
        if len(values) == 0:
            return root
        
        head = TreeNode(values[0])
        nextNode = head
        
        for i in range(1, len(values)):
            nextNode.right = TreeNode(values[i])
            nextNode = nextNode.right
        
        return head