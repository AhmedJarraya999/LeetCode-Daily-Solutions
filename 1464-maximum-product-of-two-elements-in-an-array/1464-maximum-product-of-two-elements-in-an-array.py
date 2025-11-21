class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                max_prod=max(max_prod,(nums[i]-1)*(nums[j]-1))
        return max_prod

        