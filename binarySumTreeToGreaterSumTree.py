# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def quick_sort(self, arr) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr.pop()
        valuesLower, valuesGreater = [], []
        for value in arr:
            if value < pivot:
                valuesLower.append(value)
            else:
                valuesGreater.append(value)
        return self.quick_sort(valuesLower) + [pivot] + self.quick_sort(valuesGreater)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodeValues = []
        greaterSumMap = {}
        
        def dfs(node, isConverting):
            if node is None:
                return
            if isConverting == False:
                nodeValues.append(node.val)
            else:
                node.val = greaterSumMap[node.val]
            dfs(node.left, isConverting)
            dfs(node.right, isConverting)
        
        dfs(root, False)
        nodeValues = self.quick_sort(nodeValues)
        greaterSum = 0
        counter = len(nodeValues) - 1
        
        while counter >= 0:
            value = nodeValues[counter]
            greaterSum += value
            greaterSumMap[value] = greaterSum
            counter -= 1
        
        dfs(root, True)
        return root