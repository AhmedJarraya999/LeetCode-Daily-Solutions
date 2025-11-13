class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        cnt=0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
                res=max(res,cnt)
            else:
                cnt=0
        return res
        