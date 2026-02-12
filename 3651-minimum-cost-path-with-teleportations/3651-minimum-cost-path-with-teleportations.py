class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        cost=[[inf]*m for _ in range(n)]
        cost[-1][-1]=0  
        tcost=[inf]*(max(max(row) for row in grid) +1 )
        for t in range(k+1):
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    #move right,down or teleport:
                    if i<n-1:
                        cost[i][j]=min(cost[i][j],cost[i+1][j]+grid[i+1][j])
                    if j<m-1:
                        cost[i][j]=min(cost[i][j],cost[i][j+1]+grid[i][j+1])
                    if t>0:
                        cost[i][j]=min(cost[i][j],tcost[grid[i][j]])
            #compute tcost for the next number of teleportation
            for i in range(n):
                for j in range(m):
                    tcost[grid[i][j]]=min(tcost[grid[i][j]],cost[i][j])
            for i in range(1,len(tcost)):
                tcost[i]=min(tcost[i],tcost[i-1])#compute prefix minimum
        return cost[0][0]
       