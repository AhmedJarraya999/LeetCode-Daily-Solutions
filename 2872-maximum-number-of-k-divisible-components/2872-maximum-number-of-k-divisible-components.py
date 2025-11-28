class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], nums: List[int], k: int) -> int:
        # Build adjacency list
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        self.ans = 0

        def dfs(node, parent):
            total = nums[node]

            # process children
            for nei in g[node]:
                if nei == parent:
                    continue
                total += dfs(nei, node)

            # if subtree sum divisible by k -> cut here = 1 component
            if total % k == 0:
                self.ans += 1
                return 0   # parent does not inherit this

            return total

        dfs(0, -1)
        return self.ans
