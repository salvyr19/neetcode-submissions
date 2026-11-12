class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            # je traite une simple ligne de maisons, comme dans House Robber
            if len(houses) == 1:
                return houses[0]
            max_profit = [0] * len(houses)
            max_profit[0] = houses[0]
            max_profit[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                max_profit[i] = max(max_profit[i-1], max_profit[i-2] + houses[i])
            return max_profit[-1]

        # cas 1 : je laisse la dernière maison ; cas 2 : je laisse la première
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))