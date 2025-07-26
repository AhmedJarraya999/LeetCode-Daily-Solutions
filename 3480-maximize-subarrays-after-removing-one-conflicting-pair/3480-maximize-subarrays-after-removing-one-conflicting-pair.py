class Solution:
    def maxSubarrays(self, n: int, conflicting_pairs: List[List[int]]) -> int:
        m = len(conflicting_pairs)
        # Ensure each pair is ordered (start <= end)
        for p in conflicting_pairs:
            if p[0] > p[1]:
                p[0], p[1] = p[1], p[0]
        # Sort by end-point
        conflicting_pairs.sort(key=lambda p: p[1])

        blocked = 0
        profit = 0
        max_profit = 0
        max1 = 0
        max2 = 0

        for i, (start, end) in enumerate(conflicting_pairs):
            bottom = conflicting_pairs[i+1][1] if i < m - 1 else n + 1
            gap = bottom - end

            if start > max1:
                max2 = max1
                max1 = start
                profit = 0
            elif start > max2:
                max2 = start

            profit += (max1 - max2) * gap
            if profit > max_profit:
                max_profit = profit

            blocked += max1 * gap

        total_subarrays = n * (n + 1) // 2
        return total_subarrays - blocked + max_profit