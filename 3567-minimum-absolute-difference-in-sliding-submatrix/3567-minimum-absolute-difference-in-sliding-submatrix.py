class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                values = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])
                values.sort()
                min_diff = float('inf')
                for z in range(1, len(values)):
                    if values[z] != values[z - 1]:
                        min_diff = min(min_diff, abs(values[z] - values[z - 1]))
                row.append(0 if min_diff == float('inf') else min_diff)
            result.append(row)

        return result
