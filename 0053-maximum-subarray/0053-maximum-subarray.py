class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=nums[0]
        max_sum=nums[0]
        for i,val in enumerate(nums[1:],1):
            cur_sum=max(val,cur_sum+val)
            max_sum=max(cur_sum,max_sum)
        return max_sum
