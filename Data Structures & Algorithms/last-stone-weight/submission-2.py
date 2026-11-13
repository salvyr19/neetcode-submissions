class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h ) > 1 : 
            s1, s2 = -heapq.heappop(h), -heapq.heappop(h)
            if s1 != s2 :
                s = abs(s1-s2)
                heapq.heappush(h, -s)
        return -h[0] if h else 0
        