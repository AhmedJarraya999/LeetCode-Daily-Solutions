from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # helper: total reductions for numbers 1..x
        def total_steps(x: int) -> int:
            if x <= 0:
                return 0
            res = 0
            k = 0
            base = 1
            while base <= x:
                # range [base, 4*base - 1]
                high = min(x, 4*base - 1)
                count = high - base + 1
                res += count * (k + 1)
                base *= 4
                k += 1
            return res

        ans = 0
        for l, r in queries:
            total = total_steps(r) - total_steps(l - 1)
            ans += (total + 1) // 2   # ceil division
        return ans
