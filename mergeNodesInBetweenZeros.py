# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newValues = []
        currNode = head
        mergedVal = 0
        zeroCount = 0

        while currNode is not None:
            if currNode.val == 0:
                zeroCount += 1
            else:
                mergedVal += currNode.val

            if currNode.val == 0 and zeroCount == 2:
                newValues.append(mergedVal)
                mergedVal = 0
                zeroCount = 1
            
            currNode = currNode.next
        
        currNode = head
        for i in range(len(newValues)):
            num = newValues[i]
            currNode.val = num
            if i == len(newValues) - 1:
                currNode.next = None
                break
            currNode = currNode.next
        
        return head
