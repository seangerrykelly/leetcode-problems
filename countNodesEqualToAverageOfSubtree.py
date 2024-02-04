# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Do one pass at tree and add up all of the subValues for each node
        nodeVals = []
        nodes = {}
        averageCount = 0
        def getSubtreeVals(node):
            if node is None:
                return
            nodeVals.append(node.val)
            nodes[node] = 1
            if len(nodeVals) > 1:
                nodeVals[-1] = node.val + nodeVals[len(nodeVals)-2]
            getSubtreeVals(node.left)
            getSubtreeVals(node.right)
        getSubtreeVals(root)

        # go through every node and get subtreeVals
        for node in nodes:
            nodeVals = []
            getSubtreeVals(node)
            average = nodeVals[-1] / len(nodeVals)
            if average == node.val:
                averageCount += 1
        
        return averageCount