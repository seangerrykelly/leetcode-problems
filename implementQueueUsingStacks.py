# https://leetcode.com/problems/implement-queue-using-stacks/description/
class MyQueue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue = [x] + self.queue
        

    def pop(self):
        """
        :rtype: int
        """
        frontOfQueue = self.queue.pop()
        return frontOfQueue
        

    def peek(self):
        """
        :rtype: int
        """
        # Return last element without removing it
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()