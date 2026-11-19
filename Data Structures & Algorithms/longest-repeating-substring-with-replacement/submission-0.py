class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =  0
        best = 0
        count ={}

        for r in range(0, len(s)) : 
            count[s[r]] = count.get(s[r], 0) + 1
            n_plus = max(count.values())

            while (r - l + 1) - n_plus > k : 
                count[s[l]] -= 1
                l += 1
                n_plus = max(count.values())

            best = max(best, r - l + 1)

        return best 
            




