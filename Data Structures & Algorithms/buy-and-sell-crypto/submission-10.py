class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l, r = 0, 1
        while r < len(prices) : 
            if prices[l] < prices[r] :
                best = max(best, prices[r]-prices[l])
                r +=1
            else :
                l = r
                r += 1
        return best 