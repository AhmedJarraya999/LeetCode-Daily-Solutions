class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        inc1=[float('-inf')]*len(nums)
        dec=[float('-inf')]*len(nums)
        inc2=[float('-inf')]*len(nums)
        for i in range(1,len(nums)):
            #max subarray sum ending at it foolow up order
            if nums[i]>nums[i-1]:
                inc1[i]=max(nums[i]+inc1[i-1],nums[i]+nums[i-1])
            #max subarray sum ending at it foolow up  down order
            if nums[i]<nums[i-1]:
                dec[i]=max(inc1[i-1]+nums[i],dec[i-1]+nums[i])
            #max subarray sum ending at it foolow up down up order
            if nums[i]>nums[i-1]:
                inc2[i]=max(dec[i-1]+nums[i],inc2[i-1]+nums[i])
        return max(inc2)
                
      
        