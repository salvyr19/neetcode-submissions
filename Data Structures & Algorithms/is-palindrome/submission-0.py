class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = []
        for c in s : 
            if c.isalnum():
                char.append(c.lower())
        t = "".join(char)
        t_inv = t[::-1]
        return t == t_inv