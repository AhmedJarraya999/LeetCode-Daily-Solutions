import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]  
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0

        while pq:
            t, r, c = heapq.heappop(pq)
            res = max(res, t)
            if r == n-1 and c == n-1:
                return res
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))