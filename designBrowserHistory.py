# https://leetcode.com/problems/design-browser-history/description/
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.currUrl = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[0:self.currUrl + 1]
        self.history.append(url)
        self.currUrl = len(self.history) - 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.currUrl -= steps
        if self.currUrl < 0:
            self.currUrl = 0
        
        return self.history[self.currUrl]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.currUrl += steps
        if self.currUrl >= len(self.history):
            self.currUrl = len(self.history) - 1
        
        return self.history[self.currUrl]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)