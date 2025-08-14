class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        # Initialize the sum of probabilities in the sliding window
        windowSum = 0
        for i in range(k, k + maxPts):
            if i <= n:
                windowSum += 1

        dp = {}  # dictionary: score -> probability

        # Fill dp from k-1 down to 0
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            windowSum += dp[i] - remove

        return dp[0]
