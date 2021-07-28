# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False
        
        # A map of tuples where key=node.val, value[0]=parent and value[1]=depth
        depthMap = {root.val: (None, 0)}
        
        def bfs(node, prev, level):
            if node is None:
                return
            if depthMap.get(node.val) is None:
                depthMap[node.val] = (prev.val, level)
            bfs(node.left, node, level + 1)
            bfs(node.right, node, level + 1)
        
        bfs(root.left, root, 1)
        bfs(root.right, root, 1)
        
        return depthMap[x][0] != depthMap[y][0] and depthMap[x][1] == depthMap[y][1]