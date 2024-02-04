# https://leetcode.com/problems/product-of-the-last-k-numbers/description/
# Had to do some googling on prefix products for this one
class ProductOfNumbers(object):

    def __init__(self):
        self.productList = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.productList = []
            return

        if len(self.productList) == 0:
            self.productList = [num]
        else:
            currIndex = len(self.productList) - 1
            self.productList.append(self.productList[-1] * num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == len(self.productList):
            return self.productList[-1]
        elif k > len(self.productList):
            return 0
        else:
            return self.productList[-1] / self.productList[len(self.productList) - k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)