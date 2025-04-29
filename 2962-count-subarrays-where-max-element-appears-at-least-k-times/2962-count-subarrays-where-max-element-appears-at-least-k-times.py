class Solution:
    def countSubarrays(self, nums, k):
        max_val = max(nums)
        count = 0
        freq = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == max_val:
                freq += 1
            while freq >= k:
                count += len(nums) - right
                if nums[left] == max_val:
                    freq -= 1
                left += 1
        return count
