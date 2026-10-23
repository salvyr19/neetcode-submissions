class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ens_cons = set(nums) 
        best_l = 0
        for x in ens_cons : 
            if x - 1 not in ens_cons : 
                l = 1
                while x + l in ens_cons :
                    l+=1
                best_l = max(l, best_l)
                
        return best_l 