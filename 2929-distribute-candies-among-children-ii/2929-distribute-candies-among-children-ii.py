import math

class Solution:
    def comb(self, n: int, k: int) -> int:
        if n < 0 or k < 0 or k > n:
            return 0
        return math.comb(n, k)

    def distributeCandies(self, n: int, limit: int) -> int:
        # Total number of unrestricted non-negative integer solutions to a + b + c = n
        total = self.comb(n + 2, 2)

        # Subtract cases where one variable is greater than limit
        subtract1 = 3 * self.comb(n - (limit + 1) + 2, 2)

        # Add back cases where two variables are greater than limit
        add2 = 3 * self.comb(n - 2 * (limit + 1) + 2, 2)

        # Subtract cases where all three variables are greater than limit
        subtract3 = self.comb(n - 3 * (limit + 1) + 2, 2)

        return total - subtract1 + add2 - subtract3
