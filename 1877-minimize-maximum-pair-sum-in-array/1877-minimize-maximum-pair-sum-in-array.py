class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        max_sum=0
        for i in range(len(nums)//2):
            pair_sum=nums[i]+nums[n-1-i]
            max_sum=max(max_sum,pair_sum)
        return max_sum
        






