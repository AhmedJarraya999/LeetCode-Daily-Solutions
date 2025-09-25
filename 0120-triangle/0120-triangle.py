class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows=len(triangle)


        @lru_cache(None)
        def dp(i,j):
            if i==rows-1:
                return  triangle[i][j]
            return triangle[i][j]+min(dp(i+1,j),dp(i+1,j+1))
        return dp(0,0)    
            
        