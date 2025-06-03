class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        for mask in range(1, (1 << n) - 1):  # Exclude empty set and full set
            subset = [nums[i] for i in range(n) if (mask >> i) & 1]
            complement = [nums[i] for i in range(n) if not ((mask >> i) & 1)]
        
            if prod(subset) == target and prod(complement) == target:
                return True

        return False
        
        