class Solution:
    def findMin(self, nums: List[int]) -> int:
        #solution in O(n)
        for i in range(1, len(nums)) : 
            if nums[i] < nums[i-1] : 
                return nums[i]
        return nums[0]