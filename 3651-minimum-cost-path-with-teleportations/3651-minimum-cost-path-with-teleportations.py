from typing import List
from math import inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        # cost[i][j] = minimum cost to reach destination from (i, j)
        cost = [[inf] * m for _ in range(n)]
        cost[n - 1][m - 1] = 0

        # tcost[v] = minimum cost among all cells with value <= v
        max_val = max(max(row) for row in grid)
        tcost = [inf] * (max_val + 1)

        for t in range(k + 1):
            # DP from bottom-right to top-left
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    # move down
                    if i < n - 1:
                        cost[i][j] = min(
                            cost[i][j],
                            cost[i + 1][j] + grid[i + 1][j]
                        )

                    # move right
                    if j < m - 1:
                        cost[i][j] = min(
                            cost[i][j],
                            cost[i][j + 1] + grid[i][j + 1]
                        )

                    # teleport
                    if t > 0:
                        cost[i][j] = min(
                            cost[i][j],
                            tcost[grid[i][j]]
                        )

            # recompute teleport cost array for next iteration
            for i in range(n):
                for j in range(m):
                    v = grid[i][j]
                    tcost[v] = min(tcost[v], cost[i][j])

            # prefix min so tcost[x] = min cost for any value <= x
            for v in range(1, len(tcost)):
                tcost[v] = min(tcost[v], tcost[v - 1])

        return cost[0][0]
