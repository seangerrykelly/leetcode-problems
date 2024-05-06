# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self, head):
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

    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # First reverse the linked list
        reversedHead = self.reverseLinkedList(head)

        # Now go through the list backwards, keeping track of the max
        newNodes = []
        maximum = reversedHead.val
        prev = None
        while reversedHead is not None:
            val = reversedHead.val
            if val < maximum:
                nextNode = reversedHead.next
                prev.next = nextNode
                reversedHead = prev
            elif val > maximum:
                maximum = val
                newNodes.append(val)
            else:
                newNodes.append(val)

            if reversedHead.next is None:
                break

            prev = reversedHead
            reversedHead = reversedHead.next

        # Build new linked list from newNodes list
        headClone = head
        for i in reversed(range(len(newNodes))):
            headClone.val = newNodes[i]
            if i != 0:
                headClone.next = ListNode()
                headClone = headClone.next
        return head

        