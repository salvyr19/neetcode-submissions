class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs : 
            occ_word = [0]*26
            for x in word : 
                occ_word[ord(x) - ord('a')] += 1
            key = tuple(occ_word)
            if key not in groups : 
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
            
