class Solution(object):
    def findDuplicate(self, nums):
        res=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    res=nums[i]
        return res
        