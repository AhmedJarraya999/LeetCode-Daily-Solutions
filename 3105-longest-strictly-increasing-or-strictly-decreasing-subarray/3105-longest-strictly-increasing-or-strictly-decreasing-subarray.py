class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res=inc=dec=1
        for  i in range(len(nums)):
            if  i+1<len(nums) and nums[i+1]>nums[i] :
                inc+=1
                dec=1
            elif  i+1<len(nums) and nums[i+1]<nums[i] :
                inc=1
                dec+=1
            else:
                inc=dec=1
            res=max(inc,dec,res)
            
        return res

        