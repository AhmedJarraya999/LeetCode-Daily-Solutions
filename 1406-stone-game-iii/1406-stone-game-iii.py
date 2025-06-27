class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp={}
        def dfs(i):
            if i>=len(stoneValue):
                return 0
            if i in dp:
                return dp[i]
            tot=0
            res=0 
            max_diff=float("-inf")
            for j in range(1,4):
                if i+j>len(stoneValue):
                    break
                tot+= stoneValue[i+j-1]
                max_diff=max(max_diff, tot-dfs(i+j))
            dp[i]=max_diff
            return max_diff
        diff=dfs(0)
        if diff>0:
            return "Alice"
        elif diff<0:
            return "Bob"
        else:
            return "Tie"


        