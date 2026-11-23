class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # res=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             res.append([i,j])
        # return res
        arr=sorted((num,i) for i,num in enumerate(nums))
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid][0]+arr[i][0]>target:
                    right=mid-1
                elif arr[i][0]+arr[mid][0]<target:
                    left=mid+1
                else:
                    return [arr[i][1],arr[mid][1]]





































        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # mp={}
        # for i in range(len(nums)):
        #     comp=target-nums[i]
        #     if comp in mp:
        #         return[i,mp[comp]]
        #     mp[nums[i]]=i



        # arr=sorted((num,i)for i,num in enumerate(nums))
        # for i in range(len(nums)):
        #     left=i+1
        #     right=len(arr)-1
        #     while left<=right:
        #         mid=(left+right)//2
        #         if arr[i][0]+arr[mid][0]==target:
        #             return [arr[i][1],arr[mid][1]]
        #         elif arr[i][0]+arr[mid][0]>target:
        #             right=mid-1
        #         else:
        #             left=mid+1