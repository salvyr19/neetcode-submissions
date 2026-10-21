class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_list = set() #On initialise un dictionnaire
        l = 0
        best = 0
        for r in range(len(s)) :
            while s[r] in sub_list : 
                sub_list.remove(s[l])
                l += 1
            sub_list.add(s[r])
            best = max(best, r-l+1)
        return best
                
