class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        op=0
        while nums!=sorted(nums):
            idx=1
            for i in range(2,len(nums)):
                if nums[i]+nums[i-1]<nums[idx]+nums[idx-1]:
                    idx=i
            new_nums=[]
            i=0
            while i<len(nums):
                if i==idx-1:
                    new_nums.append(nums[i]+nums[i+1])
                    i+=2
                else:
                    new_nums.append(nums[i])
                    i+=1
            nums=new_nums
            op+=1
        return op

        
        
            

   





















