class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L_occ = [[] for _ in range(len(nums)+1)]
        occ_dict = {}
        for n in nums :
            occ_dict[n] = occ_dict.get(n, 0) + 1
        for elem, freq in occ_dict.items() : 
            L_occ[freq].append(elem)
        
        res = []
        for i in range(len(L_occ)-1, 0, -1) : 
            for elem in L_occ[i]: 
                res.append(elem)
                if len(res) == k:
                    return res                
        

