class Solution(object):
    def countSubarrays(self, nums, k):
        tot_sum=0
        left=0
        count=0
        for right in range(len(nums)):
            tot_sum+=nums[right]

            while left<=right and tot_sum * (right-left+1)>=k:
                tot_sum-=nums[left]
                left+=1
            count+=(right-left+1)
        return count










        counter=0
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s*(j-i+1)<k:
                    counter+=1
        return counter
