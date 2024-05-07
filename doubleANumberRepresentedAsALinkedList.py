# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number = []
        node = head
        actualNum = 0
        currPower = 0

        while node is not None:
            number.append(node.val)
            node = node.next

        for i in reversed(range(len(number))):
            actualNum += number[i] * 10**currPower
            currPower += 1

        actualNum *= 2
        numString = str(actualNum)
        node = head
        
        for i in range(len(numString)):
            currNum = numString[i]
            node.val = int(currNum)
            if node.next is None and i != len(numString) - 1:
                node.next = ListNode()
            node = node.next
        
        return head
