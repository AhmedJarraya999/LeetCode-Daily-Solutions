class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        last = [0] * 30  # last seen position of each bit
        
        for i in range(n - 1, -1, -1):
            for j in range(30):
                if nums[i] & (1 << j):
                    last[j] = i
            max_pos = i
            for bit in range(30):
                if last[bit] != 0:
                    max_pos = max(max_pos, last[bit])
            res[i] = max_pos - i + 1
        
        return res
