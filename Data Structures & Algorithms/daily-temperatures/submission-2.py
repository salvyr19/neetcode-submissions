class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] *  len(temperatures)
        stack = [temperatures[0]]
        for i in range(1, len(temperatures)) :
            if temperatures[i] > stack[-1] :
                j = i-1
                while temperatures[i] > stack[j] and j >= 0 : 
                    if results[j] == 0 :
                        results[j] = i-j 
                    j-=1
            stack.append(temperatures[i])
        return results
