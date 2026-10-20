class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_price = prices[0]
        for price in prices :  
            best = max(best, price-min_price)
            min_price = min(price, min_price)
        return best