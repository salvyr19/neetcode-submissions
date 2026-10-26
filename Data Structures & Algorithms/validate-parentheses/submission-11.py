class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        
        if len(s) % 2 == 1 :
            return False 
        for bracket in s : 
            if bracket in "[({":
                stack.append(bracket)
            if bracket in "]})" :
                if stack : 
                    b = stack.pop()
                    if pairs[b] != bracket :
                        return False
                else :
                    return False 
        return not stack
                
