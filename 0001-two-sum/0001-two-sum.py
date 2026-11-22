class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        arr=sorted((num,i)for i,num in enumerate(nums))
        for i in range(len(nums)):
            left=i+1
            right=len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if arr[i][0]+arr[mid][0]==target:
                    return [arr[i][1],arr[mid][1]]
                elif arr[i][0]+arr[mid][0]>target:
                    right=mid-1
                else:
                    left=mid+1