# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr is not None:
            if prev is not None and curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
                continue
            else:
                prev = curr
                curr = curr.next
            
        return head
                