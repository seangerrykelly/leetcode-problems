# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, binaryString):
            if node.left is None and node.right is None:
                binaryAsInt = 0
                exponentVal = len(binaryString) - 1
                for i in binaryString:
                    binaryAsInt += int(i)*(2**exponentVal)
                    exponentVal -= 1
                numberList.append(binaryAsInt)
                return
            if node.left is not None:
                newBinaryString = binaryString + str(node.left.val)
                dfs(node.left, newBinaryString)
            if node.right is not None:
                newBinaryString = binaryString + str(node.right.val)
                dfs(node.right, newBinaryString)
        
        # Get all of the root to leaf numbers in binary and convert them to ints. Store ints in numberList
        numberList = []
        dfs(root, str(root.val))
        
        # Iterate through number list and keep track of the sum
        rootToLeafSum = 0
        for n in numberList:
            rootToLeafSum += n
        return rootToLeafSum