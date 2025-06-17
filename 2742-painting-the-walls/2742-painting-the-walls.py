class Solution:
    def paintWalls(self,cost:List[int],time:List[int])-> int:
        def dfs(i,remain):
            if remain<=0:
                return 0
            if i==len(cost):
                return float("inf")
            paint=cost[i]+dfs(i+1,remain-1-time[i])
            skip=dfs(i+1,remain )
            return min(paint,skip)
        return dfs(0,len(cost))