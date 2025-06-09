class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        i = 1

        def count(cur):
            res = 0
            nei = cur + 1
            while cur <= n:
                res += min(nei, n + 1) - cur
                cur *= 10
                nei *= 10
            return res

        while i < k:
            steps = count(cur)
            if i + steps <= k:
                cur += 1
                i += steps
            else:
                cur *= 10
                i += 1

        return cur
     
        