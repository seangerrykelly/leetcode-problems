# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDivisors(self, num):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    
    def getGreatestCommonDivisor(self, num1, num2):
        num1Divisors = self.getDivisors(num1)
        num2Divisors = self.getDivisors(num2)
        # Find common elements between arrays and return maximum
        commonDivisors = []
        i, j = 0, 0
        while i < len(num1Divisors) and j < len(num2Divisors):
            curr1, curr2 = num1Divisors[i], num2Divisors[j]
            if curr1 < curr2:
                i += 1
            elif curr1 > curr2:
                j += 1
            else:
                commonDivisors.append(curr1)
                i += 1
                j += 1
        return max(commonDivisors)

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def checkNode(node):
            if node is None or node.next is None:
                return

            # Find the greatest common divisor of the current pair
            pair = [node.val, node.next.val]
            gcd = self.getGreatestCommonDivisor(node.val, node.next.val)

            # Add new node in between node and node.next
            gcdNode = ListNode(gcd, node.next)
            node.next = gcdNode
            checkNode(gcdNode.next)

        checkNode(head)

        return head
        