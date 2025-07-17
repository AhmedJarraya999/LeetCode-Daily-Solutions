class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        # dp[i][diff] = length of sequence ending at i with difference diff
        max_len = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Extend the subsequence ending at j, or start a new one
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_len = max(max_len, dp[i][diff])

        return max_len
