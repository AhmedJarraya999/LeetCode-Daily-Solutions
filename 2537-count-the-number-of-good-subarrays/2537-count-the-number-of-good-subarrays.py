class Solution(object):
    def countGood(self,nums, k):
        count = defaultdict(int)
        left = 0
        pairs = 0
        res = 0

        for right in range(len(nums)):
            # Add nums[right] to window
            pairs += count[nums[right]]
            count[nums[right]] += 1

            # Shrink window from the left while we have enough pairs
            while pairs >= k:
                res += len(nums) - right  
                # All subarrays [left..right], [left..right+1], etc. are valid
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1

        return res
















    