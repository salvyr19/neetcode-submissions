class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        for i in range(len(prices)) : 
            for j in range(i, len(prices)) : 
                if prices[j] - prices[i] > s :
                    s = prices[j] - prices[i]
        return s