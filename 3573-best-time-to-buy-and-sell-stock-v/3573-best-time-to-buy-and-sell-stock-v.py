class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # dp[i][t][state]
        dp = [[[float('-inf')] * 3 for _ in range(k+1)] for _ in range(n)]
        
        # Base cases for day 0
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][1][2] = prices[0]

        for i in range(1, n):
            for t in range(k+1):
                # Do nothing or close transaction
                dp[i][t][0] = dp[i-1][t][0]
                if t > 0:
                    dp[i][t][0] = max(dp[i][t][0],
                                       dp[i-1][t][1] + prices[i],  # sell normal
                                       dp[i-1][t][2] - prices[i])  # buy back short
                # Buy normal
                if t > 0:
                    dp[i][t][1] = max(dp[i-1][t][1], dp[i-1][t-1][0] - prices[i])
                # Short sell
                if t > 0:
                    dp[i][t][2] = max(dp[i-1][t][2], dp[i-1][t-1][0] + prices[i])
        
        # Result is max profit with 0 stock at the end
        return max(dp[n-1][t][0] for t in range(k+1))




        