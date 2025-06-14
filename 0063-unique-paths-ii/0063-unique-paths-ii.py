class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        dp={
            (m-1,n-1):1
        }
        def dfs(r,c):
            if r==m or c==n or obstacleGrid[r][c]:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)]=dfs(r+1,c)+dfs(r,c+1)
            return dp[(r,c)]
        return dfs(0,0)

        