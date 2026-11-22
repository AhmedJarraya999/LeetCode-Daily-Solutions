class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # arr = sorted((num, i) for i, num in enumerate(nums))

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        arr=sorted((num,i) for i,num in enumerate(nums))
        for i in range(len(arr)):
            complement=target-arr[i][0]
            left=i+1
            right=len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid][0]==complement:
                    return [arr[i][1],arr[mid][1]]
                elif arr[mid][0]<complement:
                    left=mid+1
                else:
                    right=mid-1
        # for i in range(len(arr)):
        #     complement = target - arr[i][0]

        #     left = i + 1
        #     right = len(arr) - 1

        #     while left <= right:
        #         mid = (left + right) // 2

        #         if arr[mid][0] == complement:
        #             return [arr[i][1], arr[mid][1]]

        #         elif arr[mid][0] < complement:
        #             left = mid + 1

        #         else:
        #             right = mid - 1


        