# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-03-12
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        node = head
        runningSum = 0

        while node is not None:
            if node.val != 0:
                arr.append(node.val)
            node = node.next
        
        # Brute force solution
        i = 0
        while i < len(arr):
            prev = arr[i]
            runningSum += prev
            for j in range(i + 1, len(arr)):
                curr = arr[j]
                runningSum += curr
                if runningSum == 0:
                    arr = arr[:i]+arr[j+1:]
                    break
            if runningSum != 0:
                i += 1
            runningSum = 0
        
        if len(arr) == 0:
            head = None
        else:
            node = head
            currIndex = 0
            while node is not None:
                curr = arr[currIndex]
                currIndex += 1
                node.val = curr
                if currIndex >= len(arr):
                    node.next = None
                    break
                node = node.next        

        return head
