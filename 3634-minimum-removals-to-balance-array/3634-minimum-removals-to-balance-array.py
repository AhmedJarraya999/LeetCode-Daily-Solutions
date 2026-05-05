class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        left=0
        right=0
        window_size=0
        for right in range(n):
            while nums[right]>k*nums[left]:
                left+=1
            window_size=max(window_size,right-left+1)
        return n-window_size
            
        
