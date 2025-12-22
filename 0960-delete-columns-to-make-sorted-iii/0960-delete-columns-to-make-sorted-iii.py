from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        dp = [1] * m  # dp[j] = longest valid sequence ending at column j

        for j in range(m):
            for i in range(j):
                # check if column j can follow column i
                if all(strs[r][i] <= strs[r][j] for r in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)

        return m - max(dp)
