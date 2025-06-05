class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_suffix = [0] * n
        max_suffix[-1] = nums[-1]

        # Precompute max suffix from the right
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(max_suffix[i + 1], nums[i])

        max_result = 0
        max_left = nums[0]

        for j in range(1, n - 1):
            value = (max_left - nums[j]) * max_suffix[j + 1]
            max_result = max(max_result, value)
            max_left = max(max_left, nums[j])  # update for next j

        return max_result
        