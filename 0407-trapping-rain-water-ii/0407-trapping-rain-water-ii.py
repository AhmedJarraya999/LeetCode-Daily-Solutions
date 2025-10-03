import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Step 1: push all boundary cells
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        maxHeight = 0
        
        # Step 2: process heap
        while heap:
            height, x, y = heapq.heappop(heap)
            maxHeight = max(maxHeight, height)
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if heightMap[nx][ny] < maxHeight:
                        water += maxHeight - heightMap[nx][ny]
                    heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
        
        return water
