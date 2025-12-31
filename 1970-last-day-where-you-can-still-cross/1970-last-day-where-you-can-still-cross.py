class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day):
            directions=directions = [(1,0), (-1,0), (0,1), (0,-1)]
            grid=[[0]*col for _ in range(row)]
            for i in range(day):
                r,c=cells[i]
                grid[r-1][c-1]=1
            q=deque()
            visited=[[False]*col for _ in range(row)]
            #start from top row
            for c in range(col):
                if grid[0][c]==0:
                    q.append((0,c))
                    visited[0][c] = True
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            q.append((nr, nc))

            return False
            
        left=1
        right=row*col
        ans=0
        while left<=right:
            mid = (left + right) // 2
            if canCross(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans


        # def can_reach_end():
        #     directions = [(0,1), (1,0), (0,-1), (-1,0)]
        #     visited = [[False]*col for _ in range(row)]
        #     queue = deque([(0,0)])
        #     visited[0][0] = True
        #     while queue:
        #         x,y=queue.popleft()
        #         if x==row-1 and y==col-1:
        #             return True
        #         for dx,dy in directions:
        #             nx, ny = x + dx, y + dy
        #         if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 0:
        #             queue.append((nx, ny))
        #             visited[nx][ny] = True
        #     return False


        