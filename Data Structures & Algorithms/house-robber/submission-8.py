class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        max_profit = [0]*(len(nums))
        max_profit[0] = nums[0]
        max_profit[1] = nums[1]
        for i in range(2, len(nums)) : 
            max_profit[i] = max(max_profit[:i-1]) + nums[i]

        return max(max_profit)
