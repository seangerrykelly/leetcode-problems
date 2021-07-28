# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def dfs(node, array):
            if node is None:
                array.append(None)
                return
            else:
                array.append(node.val)
                dfs(node.left, array)
                dfs(node.right, array)
        
        pArray = []
        qArray = []
        dfs(p, pArray)
        dfs(q, qArray)
        
        return pArray == qArray