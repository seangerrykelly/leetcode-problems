# https://leetcode.com/problems/simple-bank-system/description/
class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.accounts = {}
        for i in range(len(balance)):
            self.accounts[i+1] = balance[i]
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 not in self.accounts or account2 not in self.accounts:
            return False
        if money <= self.accounts[account1]:
            self.accounts[account1] -= money
            self.accounts[account2] += money
            return True
        else:
            return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account not in self.accounts:
            return False
        else:
            self.accounts[account] += money
            return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account not in self.accounts:
            return False
        elif money <= self.accounts[account]:
            self.accounts[account] -= money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)