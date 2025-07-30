class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest = count = 0
        
        for num in nums:
            if num == max_val:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
        
        return longest
