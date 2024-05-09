# https://leetcode.com/problems/design-hashmap/description/
class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            for i in range(len(self.keys)):
                mapKey = self.keys[i]
                if mapKey == key:
                    self.values[i] = value
                    break
                else:
                    continue  

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        else:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    return self.values[i]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                self.values.pop(i)
                break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)