# https://leetcode.com/problems/reorder-list/description/?envType=daily-question&envId=2024-03-23
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodeVals = []
        curr = head
        while curr is not None:
            nodeVals.append(curr.val)
            curr = curr.next
        
        # Reorder the list using left + right pointers
        curr = head
        left, right = 0, len(nodeVals) - 1
        isLeft = True

        while curr is not None:
            if isLeft:
                isLeft = False
                curr.val = nodeVals[left]
                left += 1
                curr = curr.next
            else:
                isLeft = True
                curr.val = nodeVals[right]
                right -= 1
                curr = curr.next
        
        return head