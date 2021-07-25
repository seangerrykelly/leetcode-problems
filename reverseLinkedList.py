# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        nextNode = head.next
        previousNode = head
        head.next = None
        head = nextNode
        
        while True:
            if head.next is None:
                head.next = previousNode
                break
            nextNode = head.next
            head.next = previousNode
            previousNode = head
            head = nextNode
            
        return head