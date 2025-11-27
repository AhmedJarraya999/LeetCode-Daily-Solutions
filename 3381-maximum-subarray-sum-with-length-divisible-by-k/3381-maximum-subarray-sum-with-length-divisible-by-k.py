class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix = 0
        min_pref=[float('inf')] *k
        min_pref[0]=0
        best = -10**30
        for i, val in enumerate(nums,1):
            prefix+=val
            r=i%k
            best=max(best,prefix-min_pref[r])
            min_pref[r] = min(min_pref[r], prefix)
        return best



        