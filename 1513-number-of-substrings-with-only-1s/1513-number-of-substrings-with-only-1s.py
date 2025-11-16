class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        res = 0

        for c in s:
            if c == '1':
                count += 1
            else:
                res = (res + count * (count + 1) // 2) % MOD
                count = 0

        # add last block of 1s
        res = (res + count * (count + 1) // 2) % MOD
        return res
