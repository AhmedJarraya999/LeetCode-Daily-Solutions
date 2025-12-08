import math

class Solution:
    def countTriples(self, n: int) -> int:
        nb = 0
        for a in range(1, n):
            for b in range(1,n):
                c2 = a*a + b*b
                c = math.isqrt(c2)
                if c <= n and c*c == c2:
                    nb += 1
        return nb
