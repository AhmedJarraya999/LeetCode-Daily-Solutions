from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        ans = [[-1]*cols for _ in range(rows)]
        q = deque()
        
        # Start BFS from all water cells
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i,j))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and ans[nr][nc]==-1:
                    ans[nr][nc] = ans[r][c]+1
                    q.append((nr,nc))
        return ans
