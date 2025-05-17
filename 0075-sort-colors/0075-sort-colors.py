class Solution(object):
    def sortColors(self, nums):
        lr=[]
        lb=[]
        lw=[]
        for i in range(len(nums)):
            if nums[i]==0:
                lr.append(nums[i])
            elif nums[i]==1:
                lw.append(nums[i])
            else:
                lb.append(nums[i])
        for i in range(len(nums)):
            if i<len(lr):
                nums[i]=0
            elif i<len(lr)+len(lw):
                nums[i]=1
            else:
                nums[i]=2
        return nums


        