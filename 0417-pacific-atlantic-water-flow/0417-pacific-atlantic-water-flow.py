class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        atlantic=set()
        pacific=set()
        visited=set()
        def dfs(r,c,visited,prevHeight):
            if (r<0 or c<0 or r==rows or c==cols or(r,c) in visited or heights[r][c]<prevHeight):
                return
            visited.add((r,c))
            directions=[[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])
        #dfs for all pacific cells
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])      # left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  
        result = list(pacific & atlantic)
        return result

    
        