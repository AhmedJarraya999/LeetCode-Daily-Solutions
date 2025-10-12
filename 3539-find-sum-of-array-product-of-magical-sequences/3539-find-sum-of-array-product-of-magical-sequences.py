from typing import List
import math

class Solution:
    MOD = 10**9 + 7

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        MOD = self.MOD

        # Precompute factorials and inv factorials up to m
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD-2, MOD)
        for i in range(m-1, -1, -1):
            invfact[i] = invfact[i+1] * (i+1) % MOD

        def comb(a, b):
            if b < 0 or b > a: return 0
            return fact[a] * invfact[b] % MOD * invfact[a-b] % MOD

        # Precompute nums[j]^c for c=0..m
        pownums = [[1] * (m + 1) for _ in range(n)]
        for j in range(n):
            for c in range(1, m + 1):
                pownums[j][c] = pownums[j][c-1] * (nums[j] % MOD) % MOD

        # Determine how many bit positions we need to process.
        # If all m picks go to highest index (n-1), the top bit index can be up to n-1 + floor(log2(m))
        # we'll add a couple extra bits for safety.
        extra = (m.bit_length() if m > 0 else 1)
        maxbit = n + extra + 2  # number of bit positions to process

        # dp[s][carry][t] = value
        # s: picks used so far (0..m)
        # carry: carry into current bit (0..m)
        # t: number of set bits so far (0..k)
        # use rolling arrays for bit positions
        dp_cur = [ [ [0] * (k+1) for _ in range(m+1) ] for __ in range(m+1) ]
        dp_next = [ [ [0] * (k+1) for _ in range(m+1) ] for __ in range(m+1) ]

        dp_cur[0][0][0] = 1

        for j in range(maxbit):
            # reset dp_next
            for s in range(m+1):
                for carry in range(m+1):
                    for tval in range(k+1):
                        dp_next[s][carry][tval] = 0

            for s in range(m+1):
                remain = m - s
                for carry in range(m+1):
                    for tval in range(k+1):
                        val = dp_cur[s][carry][tval]
                        if val == 0:
                            continue

                        # If j < n, we can allocate cj from 0..remain
                        # If j >= n, no more nums to assign: cj must be 0
                        max_cj = remain if j < n else 0
                        for cj in range(max_cj + 1):
                            new_s = s + cj
                            new_sum = cj + carry
                            bit_here = new_sum & 1
                            new_t = tval + bit_here
                            if new_t > k:
                                continue
                            new_carry = new_sum >> 1
                            if new_carry > m:
                                continue

                            # multiply val by C(remain, cj) (choosing which positions among remaining picks)
                            ways = val * comb(remain, cj) % MOD
                            # multiply by nums[j]^cj (if j < n)
                            if j < n and cj > 0:
                                ways = ways * pownums[j][cj] % MOD

                            dp_next[new_s][new_carry][new_t] = (dp_next[new_s][new_carry][new_t] + ways) % MOD

            # swap
            dp_cur, dp_next = dp_next, dp_cur

        # result: all m picks used, no remaining carry, exactly k set bits
        return dp_cur[m][0][k] % MOD
