class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        cnt=defaultdict(int)
        for w in words:
            for i,c in enumerate(w):
                cnt[(i,c)]+=1
        dp={}#map i,j to num f ways we can build the target word
        #i index of target j index of word
        def dfs(i,j):
            if i==len(target):
                return 1
            if j==len(words[0]):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            c=target[i]
            dp[(i,j)]=dfs(i,j+1)# skip i position
            dp[(i,j)]+=cnt[(j,c)] * dfs(i+1,j+1)
            return dp[(i,j)]%(10**9+7)
        return dfs(0,0)
            


                


        

        