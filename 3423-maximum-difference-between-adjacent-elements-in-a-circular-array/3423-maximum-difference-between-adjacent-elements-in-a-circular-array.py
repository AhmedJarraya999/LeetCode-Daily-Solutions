class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff=float(-inf)
        n=len(nums)
        for i in range(n-1):
            if abs(nums[i+1]- nums[i])>max_diff:
                max_diff=abs(nums[i+1]- nums[i])
        if abs(nums[n-1]-nums[0])>max_diff:
            max_diff=abs(nums[n-1]-nums[0])
        return max_diff
        