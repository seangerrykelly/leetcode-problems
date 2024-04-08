# https://leetcode.com/problems/merge-in-between-linked-lists/description/?envType=daily-question&envId=2024-03-23
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        nodeCount = 0
        startNode, endNode = None, None
        curr1, curr2 = list1, list2

        # First go through the list and find the start and end nodes
        while curr1 is not None:
            if nodeCount == a - 1:
                startNode = curr1
            if nodeCount == b + 1:
                endNode = curr1
            curr1 = curr1.next
            nodeCount += 1
        
        curr1 = list1
        nodeCount = 0
        shouldExit = False

        while curr1 is not None:
            if curr1 == startNode:
                # Now merge the second list
                while curr2 is not None:
                    curr1.next = curr2
                    curr1 = curr1.next
                    curr2 = curr2.next

                if curr2 is None:
                    # Add the endNode and exit the loop
                    curr1.next = endNode
                    shouldExit = True
                    break
            
            if shouldExit:
                break
                
            nodeCount += 1
            curr1 = curr1.next
        
        return list1
