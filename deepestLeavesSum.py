# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def bfs(node, level):
            if node is None:
                return
            if depthMap.get(level) is None:
                depthMap[level] = [node.val]
            else:
                depthMap[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        leafSum = 0
        deepestLevel = 0
        depthMap = {}
        bfs(root, deepestLevel)
        for key in depthMap:
            if key > deepestLevel:
                deepestLevel = key
        for i in depthMap[deepestLevel]:
            leafSum += i
        
        return leafSum