class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        abc = 6  
        aba = 6 

        for _ in range(2, n + 1):
            new_abc = (2 * abc + 2 * aba) % MOD
            new_aba = (2 * abc + 3 * aba) % MOD
            abc, aba = new_abc, new_aba

        return (abc + aba) % MOD
