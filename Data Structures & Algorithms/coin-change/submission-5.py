class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] la plus petite façon de former la pièce i à partir de coin
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)) :
            dp[i] = 1 + min([dp[i-c] for c in coins if i-c>=0 ], default = float('inf'))
        return dp[-1] if dp[-1] != float('inf') else -1

