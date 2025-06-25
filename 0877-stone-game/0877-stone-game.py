class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp={} #(l,r)->max alice total
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            even=True if (r-l)%2 else False
            left=piles[l] if even else 0 #we take  left only if alice turn
            right=piles[r] if even else 0 #we take right case only if alice turn
            right=piles[r]
            dp[(l,r)]=max(dfs(l+1,r)+left,
            dfs(l,r-1)+right)
            return dp[(l,r)]
        return dfs(0,len(piles)-1)>sum((piles))//2
        