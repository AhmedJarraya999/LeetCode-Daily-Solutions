class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 1

        for target in range(k):  # try all possible values of (a + b) % k
            dp = [1] * n  # dp[i] = length of longest subsequence ending at index i
            for i in range(n):
                for j in range(i):
                    if (nums[j] + nums[i]) % k == target:
                        dp[i] = max(dp[i], dp[j] + 1)
                max_len = max(max_len, dp[i])

        return max_len
        