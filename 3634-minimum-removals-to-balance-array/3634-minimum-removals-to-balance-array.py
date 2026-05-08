class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        def binarysearch(target):
            left=0
            right=len(nums)
            while left<right:
                mid=(left+right)//2
                if nums[mid]<=k*nums[i]:
                    left=mid+1
                else:
                    right=mid
            return left
        window=0
        for i in range(len(nums)):
            j=binarysearch(nums[i]*k)
            window=max(window,j-i)
        return n-window
        