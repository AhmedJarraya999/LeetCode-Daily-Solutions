class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = abs(n)
        ans = 1.0

        while p > 0:
            if p & 1:
                ans *= x
            x *= x
            p //= 2
        return 1 / ans if n < 0 else ans
