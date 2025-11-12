from math import gcd

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        total_gcd = 0
        for num in nums:
            total_gcd = gcd(total_gcd, num)
        
        # If overall gcd != 1 → impossible
        if total_gcd != 1:
            return -1
        
        # If there's already a 1 → just make all others 1
        if 1 in nums:
            return n - nums.count(1)
        
        # Otherwise, find shortest subarray with gcd == 1
        min_len = float('inf')
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i+1, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return min_len + n - 2
