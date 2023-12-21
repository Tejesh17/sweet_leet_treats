class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if(len(prices)<2):
            return money
        prices.sort()
        og = money
        money -= (prices[0]+prices[1])
        if(money<0):
            return og
        return money