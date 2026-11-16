class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # je m'arrête si la somme devient négative en incluant un nombre 
        if len(nums) == 1 :
            return nums[0]
        max_sum = nums[0]
        cur = 0
        for n in nums :
            cur += n
            max_sum = max(cur, max_sum)
            if cur < 0 :
                cur = 0
        return max_sum

