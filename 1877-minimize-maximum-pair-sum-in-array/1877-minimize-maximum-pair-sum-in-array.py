class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()  # Step 1: sort the array
        n = len(nums)
        max_sum = 0

        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]  # pair smallest with largest
            max_sum = max(max_sum, pair_sum)      # track the maximum pair sum

        return max_sum
