class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp={}
        def dfs (alice,i,M):#Alice Score
            if i==len(piles):
                return 0
            if (alice,i,M) in dp:
                return dp[(alice,i,M)]
            tot=0
            res=0 if alice else float("inf")
            for X in range(1,2*M+1):
                if i+X>len(piles):
                    break
                tot+=piles[i+X-1]
                if alice:
                    res=max(res,tot+dfs(not alice,i+X,max(M,X)))
                else:
                    res=min(res,dfs(not alice,i+X,max(M,X)))
            dp[(alice,i,M)]=res
            return res
        return dfs(True,0,1)
                
               