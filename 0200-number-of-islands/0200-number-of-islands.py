import collections

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    rr, cc = row + dr, col + dc
                    if (0 <= rr < rows and 0 <= cc < cols and 
                        grid[rr][cc] == "1" and (rr, cc) not in visit):
                        q.append((rr, cc))
                        visit.add((rr, cc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    res += 1

        return res
