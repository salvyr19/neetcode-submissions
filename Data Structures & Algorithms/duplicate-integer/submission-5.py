class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for n in nums :
            if n not in h :
                h.add(n)
            else : 
                return True
        return False