class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] *  len(temperatures)
        stack = []
        for i, t in enumerate(temperatures) :
            while stack and t > temperatures[stack[-1]] : 
                j = stack.pop()
                results[j] = i - j

            stack.append(i)
        return results
