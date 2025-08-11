class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        powers = []
        pos = 0
        while n:
            if n % 2 == 1:
                powers.append(2 ** pos)
            n //= 2
            pos += 1
        
        for i in range(1, len(powers)):
            powers[i] *= powers[i - 1]
        
        res = []
        for l, r in queries:
            curr = powers[r]
            if l > 0:
                curr //= powers[l - 1]
            res.append(curr % MOD)
        
        return res
