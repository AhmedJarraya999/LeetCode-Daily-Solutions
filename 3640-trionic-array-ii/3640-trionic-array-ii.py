class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ##max subarray ending at i followingg inc shape
        inc1=[float("-inf")]*len(nums)
        ##max subarray ending at i following inc then dec shape
        dec=[float("-inf")]*len(nums)
        ##max subarray ending at i following in dec then inc again shape 
        inc2=[float("-inf")]*len(nums)
        for  i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc1[i]=max(inc1[i-1]+nums[i],nums[i]+nums[i-1])
            if nums[i]<nums[i-1]:
                dec[i]=max(inc1[i-1]+nums[i],dec[i-1]+nums[i])
            if nums[i]>nums[i-1]:
                inc2[i]=max(dec[i-1]+nums[i],inc2[i-1]+nums[i])
        return max(inc2)
        