class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]
        dp=[[0]*n for _ in range(n)]
        dp[row][column] = 1.0
        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp[i][j]>0:
                        for dx,dy in moves:
                            ni,nj=i+dx,j+dy
                            if 0<=ni<n and 0<=nj<n:
                                new_dp[ni][nj]+=dp[i][j]/8
            dp=new_dp
        return sum(sum(row) for row in dp)


        