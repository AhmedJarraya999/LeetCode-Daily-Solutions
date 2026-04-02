class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int: 
        i=0
        res=float('-inf')
        while i<len(nums):
            j=i+1
            ##first segmentsum
            while j<len(nums) and nums[j]>nums[j-1]:
                j+=1
            p=j-1
            if p==i:
                i+=1
                continue
            cur=nums[p]+nums[p-1]
            ## second segment sum
            while j<len(nums) and nums[j]<nums[j-1]:
                cur+=nums[j]
                j+=1
            q=j-1
            if p==q or q==len(nums)-1 or nums[q]==nums[j]:
                i=q
                continue
            cur+=nums[j]
            j+=1
            cum=0
            mx=0
            while j<len(nums) and nums[j]>nums[j-1]:
                cum+=nums[j]
                mx=max(mx,cum)
                j+=1
            cur+=mx
            jj=p-2
            acc=0
            mx=0
            while jj>=0 and nums[jj]<nums[jj+1]:
                acc+=nums[jj]
                mx=max(acc,mx)
                jj-=1
            cur+=mx
            res=max(res,cur)
            i=q
        return res


            

        
                

                
        
        
            


        
            
            
