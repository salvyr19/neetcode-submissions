class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            # step 1 : on trie le tableau sur place
            nums.sort()  # complexité O(n log n)
            # step 2 : on utilise l'algorithme de 2sum
            L_0 = []
            for i in range(len(nums)):
                # je saute une valeur de i déjà traitée, sinon je retrouve les mêmes triplets
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                target = -nums[i]
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        L_0.append([nums[i], nums[l], nums[r]])
                        l += 1
                        # je saute les valeurs de l identiques à celle que je                                   viens                     d'utiliser
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
            return L_0  
