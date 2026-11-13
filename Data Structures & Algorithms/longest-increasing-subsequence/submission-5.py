class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] la plus longue sequence depuis i
        if len(nums) ==  1 :
            return 1
        dp = [0]*len(nums)
        dp[-1] = 1
        for i in range(len(nums)-2, -1, -1) :
            dp[i] = 1 + max([dp[k] for k in range(i+1, len(nums)) if nums[k] > nums[i]], default = 0)    
        
        return max(dp)