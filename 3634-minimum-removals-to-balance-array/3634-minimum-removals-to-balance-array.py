class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        def binarysearch(target):
            left,right=0,len(nums)
            while left<right:
                mid=(left+right)//2
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid
            return left
        nums.sort()
        n=len(nums)
        window_size=0
        for i in range(n):
            # find first index where value > k * nums[i]
            # j=bisect_right(nums,k*nums[i])
            j=binarysearch(k*nums[i])
            ##window is [i,j-1]
            window_size=max(window_size,j-i)
        return n- window_size
        # nums.sort()
        # n=len(nums)
        # left=0
        # right=0
        # window_size=0
        # for right in range(n):
        #     while nums[right]>k*nums[left]:
        #         left+=1
        #     window_size=max(window_size,right-left+1)
        # return n-window_size
            
        
