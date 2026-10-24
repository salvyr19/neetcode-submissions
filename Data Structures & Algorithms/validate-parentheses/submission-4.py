class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        if len(s) % 2 == 1 : 
            return False 
        for b in s :
            if b in "[{(" : 
                stack.append(b)
            if b in "]})" : 
                if stack :
                    op_b = stack.pop() 

                    if not op_b == pairs[b] :
                        return False  
                else : 
                    return False
        return not stack