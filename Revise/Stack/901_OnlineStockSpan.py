class StockSpanner:

    def __init__(self):
        self.stack = [] #[ind, price]
        self.i=0

    def next(self, price: int) -> int:
        while(self.stack and self.stack[-1][1]<=price):
            self.stack.pop()
        self.i +=1
        ans = self.i
        if self.stack:
            ans= (self.i)- self.stack[-1][0]
        self.stack.append([self.i, price])
        return (ans)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)