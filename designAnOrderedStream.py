# https://leetcode.com/problems/design-an-ordered-stream/description/
class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.orderedStream = {i: "" for i in range(n+1)}
        self.pointer = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        result = []
        self.orderedStream[idKey] = value
        if self.pointer == idKey:
            while self.pointer in self.orderedStream and len(self.orderedStream[self.pointer]) > 0:
                result.append(self.orderedStream[self.pointer])
                self.pointer += 1
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)