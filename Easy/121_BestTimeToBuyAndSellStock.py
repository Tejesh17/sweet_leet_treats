class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if(profit> 0):
        #             res = max(profit, res)
        # return res

        l,h = 0,1
        profit = 0
        while(h <len(prices)):
            profit = max(profit, prices[h]-prices[l])
            if(prices[h] < prices[l]):
                l = h
                h+=1
            else:
                h+=1
        return profit