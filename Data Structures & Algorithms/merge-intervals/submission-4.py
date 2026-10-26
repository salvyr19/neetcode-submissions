class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        s = [intervals[0]]
        for interval in intervals : 
            if interval[0] <= s[-1][1] : 
                s[-1][1] = max(interval[1], s[-1][1])
            else :
                s.append(interval)
        return s