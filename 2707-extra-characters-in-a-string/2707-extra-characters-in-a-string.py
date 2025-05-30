class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set=set(dictionary)
        n=len(s)
        def dp(i):
            if i==n:
                return 0
            res=1+dp(i+1)

            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    res = min(res, dp(j)) 
            return res  
        return dp(0)