class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h = []
        results = [0]*len(temperatures)
        for i, t in enumerate(temperatures) :

            while h and t  > temperatures[h[-1]]:
                j = h.pop()
                results[j] = i-j

            h.append(i)
        
        return results
            
