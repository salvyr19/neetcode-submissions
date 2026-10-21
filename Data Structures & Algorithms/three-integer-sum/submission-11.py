class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # step 1 :  on trie le tableau 
        nums_trier = sorted(nums) #complexité O(nlog(n))
        #step 2 : on utilise l'algorithme de 2sum
        L_0 = [] #On initialise une liste qui contient les 3sums
        for i in range(len(nums_trier)): 
            if i > 0 and nums_trier[i] == nums_trier[i - 1]:
                continue
            target  = -nums_trier[i]
            l = i+1
            r = len(nums_trier)-1
            while l < r : 
                if nums_trier[l] + nums_trier[r] > target :
                    r -= 1
                elif nums_trier[l] + nums_trier[r] < target :
                    l+=1 
                else : 
                    L_0.append([nums_trier[i], nums_trier[l], nums_trier[r]])
                    l+=1
                    while l<r and nums_trier[l] == nums_trier[l-1]:
                        l+=1
        return L_0 
                    
