# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getLinkedListNum(self, l):
        currPower = 0
        num = 0
        while l is not None:
            curr = l.val
            num += (curr*10**currPower)
            currPower += 1
            l = l.next
        return num

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = self.getLinkedListNum(l1), self.getLinkedListNum(l2)
        listSum = str(num1 + num2)
        lTotal = ListNode()
        clone = lTotal
        
        for i in reversed(range(len(listSum))):
            curr = int(listSum[i])
            clone.val = curr
            if i == 0:
                break
            clone.next = ListNode()
            clone = clone.next
        return lTotal


        