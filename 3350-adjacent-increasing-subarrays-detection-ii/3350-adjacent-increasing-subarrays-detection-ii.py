class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: increasing lengths ending at each i
        left = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1
        
        # Step 2: increasing lengths starting at each i
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1
        
        # Step 3: find max possible k
        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(left[i], right[i + 1]))
        
        return ans
