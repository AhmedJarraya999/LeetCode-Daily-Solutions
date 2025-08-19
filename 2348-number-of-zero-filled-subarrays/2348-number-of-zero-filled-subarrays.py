class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
                res+=count
            else:
                count=0
        return res
        