class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum=sum(stones)
        target=ceil(stonesSum/2)#rounded
        dp={}
        def dfs(i,totcur):
            if totcur>=target or i==len(stones):
                return abs(totcur-(stonesSum-totcur))#other pile 
            if (i,totcur)in dp:
                return dp[(i,totcur)]
            dp[(i, totcur)] = min(
                dfs(i + 1, totcur),              # don't take the stone
                dfs(i + 1, totcur + stones[i])   # take the stone
            )
            return dp[(i, totcur)]
        return dfs(0,0)
            



        
        