class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = Counter(nums)
        left = 0
        total = len(nums)
        ans = 0
        
        for v in count.values():
            total -= v           # remaining elements
            ans += left * v * total
            left += v            # move current group to left
        
        return ans
        