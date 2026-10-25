class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count  = {0 : 1}
        curSum = 0
        res =0
        for n in nums :
            curSum += n
            diff = curSum - k

            res += count.get(diff, 0)
            count[curSum] = count.get(curSum, 0) + 1 
        return res

