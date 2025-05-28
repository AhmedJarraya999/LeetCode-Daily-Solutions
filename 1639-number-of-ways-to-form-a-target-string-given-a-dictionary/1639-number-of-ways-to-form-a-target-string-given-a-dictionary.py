MOD = 10**9 + 7

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)

        for w in words:
            for i, c in enumerate(w):
                cnt[(i, c)] += 1

        dp = {}  # memoization: (i, k) → number of ways to build target[i:] from words[k:]

        def dfs(i, k):
            if i == len(target):
                return 1
            if k == len(words[0]):
                return 0
            if (i, k) in dp:
                return dp[(i, k)]

            res = dfs(i, k + 1)  # skip column k
            c = target[i]
            res += cnt[(k, c)] * dfs(i + 1, k + 1)
            res %= MOD

            dp[(i, k)] = res
            return res

        return dfs(0, 0)
