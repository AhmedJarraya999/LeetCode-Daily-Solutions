class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int: 
        nums.sort()
        n=len(nums)
        window=0
        #
        def binarysearch(target):
            left=0
            right=len(nums)
            while left<right:
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid
                else:
                    left=mid+1
            return left

        for i in range(n):
            j=binarysearch(nums[i]*k)
            window=max(window,j-i)
        return n-window

        