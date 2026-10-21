class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        for i, p in enumerate(prices) : 
            if p < prices[l] :
                l = i
            best = max(best, p - prices[l]) 
        return best
        
