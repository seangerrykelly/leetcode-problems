class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.customerCount = 0
        self.productPriceMap = {}
        for i in range(len(products)):
            product, price = products[i], prices[i]
            if product not in self.productPriceMap:
                self.productPriceMap[product] = price
        

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.customerCount += 1
        bill = 0
        for i in range(len(product)):
            currProduct, currAmount = product[i], amount[i]
            productPrice = self.productPriceMap[currProduct]
            bill += (currAmount*productPrice)
            
        if self.customerCount == self.n:
            bill = bill*((100.0 - self.discount) / 100.0)
            self.customerCount = 0

        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)