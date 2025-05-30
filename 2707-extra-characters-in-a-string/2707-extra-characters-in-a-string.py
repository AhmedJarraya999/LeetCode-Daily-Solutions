class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set=set(dictionary)
        n=len(s)
        dp={}
        def dfs(i):
            if i==n:
                return 0
            if i in dp:
                return dp[i]
            res=1+dfs(i+1)

            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    res = min(res, dfs(j))
            dp[i]=res 
            return res  
        return dfs(0)