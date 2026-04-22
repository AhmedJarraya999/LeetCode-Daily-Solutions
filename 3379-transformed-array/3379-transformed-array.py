class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                index=(i+nums[i])%len(nums)
                result[i]=nums[index]
            if nums[i]<0:
                index=(i-abs(nums[i]))%len(nums)
                #index = (i + nums[i]) % len(nums)
                result[i]=nums[index]
            if nums[i]==0:
                result[i]=nums[i]
        return result
        
        