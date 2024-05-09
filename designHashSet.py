# https://leetcode.com/problems/design-hashset/description/
class MyHashSet(object):

    def __init__(self):
        self.keys = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return
        else:
            self.keys.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.keys:
            return
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                return

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.keys
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)