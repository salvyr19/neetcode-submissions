class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):

            max_profit_prev2, max_profit_prev1 = 0, 0
            for x in houses:
                # je laisse la maison ou je la vole
                max_profit_prev2, max_profit_prev1 = max_profit_prev1, max(max_profit_prev1, max_profit_prev2 + x)
            return max_profit_prev1

        # cas 1 : je laisse la dernière maison ; cas 2 : je laisse la première
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))