class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int: 
        res=float('-inf')
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums) and nums[j]>nums[j-1]:
                j+=1
            p=j-1
            if p==i:
                i+=1
                continue
            curr=nums[p]+nums[p-1]
            while j<len(nums) and nums[j]<nums[j-1]:
                curr+=nums[j]
                j+=1
            q=j-1
            if p==q or q==len(nums)-1 or (q<len(nums) and nums[q]==nums[j]):
                i=q
                continue
            curr+=nums[j]
            j+=1
            cum=0
            mx=0
            while j<len(nums) and nums[j]>nums[j-1]:
                cum+=nums[j]
                mx=max(mx,cum)
                j+=1
            curr+=mx
            jj=p-2
            cum=0
            mx=0
            while jj>=0 and nums[jj]<nums[jj+1]:
                cum+=nums[jj]
                mx=max(cum,mx)
                jj-=1
            curr+=mx
            res=max(res,curr)
            i=q
        return res
            



            
            


        
            
            
