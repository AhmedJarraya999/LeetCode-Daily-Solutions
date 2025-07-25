class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique=set(nums)
        mx=max(unique)
        unique.remove(mx)
        res=mx
        for val in unique:
            res=max(res,res+val)
        return res
        