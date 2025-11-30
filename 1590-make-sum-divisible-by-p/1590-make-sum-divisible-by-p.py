class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        prefix_map = {0: -1}  # modulo -> index
        curr = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            curr = (curr + num) % p
            # we want a previous prefix such that (curr - prev) % p == target
            needed = (curr - target + p) % p
            if needed in prefix_map:
                min_len = min(min_len, i - prefix_map[needed])
            prefix_map[curr] = i
        
        return min_len if min_len < len(nums) else -1
