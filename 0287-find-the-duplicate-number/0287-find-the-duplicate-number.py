class Solution(object):
    def findDuplicate(self, nums):
        res=-1
        checker=set()
        for i in range(len(nums)):
            if nums[i] not in checker:
                checker.add(nums[i])
            else:
                res=nums[i]
        return res
        