class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Initialize prefix sums
        pp = [prices[0]] * n
        ps = [strategy[0] * prices[0]] * n

        for i in range(1, n):
            pp[i] = pp[i - 1] + prices[i]
            ps[i] = ps[i - 1] + (strategy[i] * prices[i])

        res = ps[-1]

        for i in range(k - 1, n):
            curr = ps[i] - (ps[i - k] if i - k >= 0 else 0)
            change = pp[i] - (pp[i - k // 2] if i - k // 2 >= 0 else 0)
            res = max(res, ps[-1] - curr + change)

        return res
        