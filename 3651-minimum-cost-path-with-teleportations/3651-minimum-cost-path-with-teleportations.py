from math import inf
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])

        cost = [[inf] * m for _ in range(n)]
        cost[n - 1][m - 1] = 0

        max_val = max(max(row) for row in grid)
        tcost = [inf] * (max_val + 1)

        for t in range(k + 1):
            # normal DP
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if i + 1 < n:
                        cost[i][j] = min(
                            cost[i][j],
                            grid[i + 1][j] + cost[i + 1][j]
                        )
                    if j + 1 < m:
                        cost[i][j] = min(
                            cost[i][j],
                            grid[i][j + 1] + cost[i][j + 1]
                        )
                    if t > 0:
                        cost[i][j] = min(
                            cost[i][j],
                            tcost[grid[i][j]]  # teleport cost = 0
                        )

            # update teleport helper
            for i in range(n):
                for j in range(m):
                    v = grid[i][j]
                    tcost[v] = min(tcost[v], cost[i][j])

            # prefix min so <= condition is satisfied
            for v in range(1, len(tcost)):
                tcost[v] = min(tcost[v], tcost[v - 1])

        return cost[0][0]
