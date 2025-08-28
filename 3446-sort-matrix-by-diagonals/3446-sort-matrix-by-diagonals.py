class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        diags=defaultdict(list)
        n=len(grid)
        for r in range(n):
            for c in range(n):
                diags[r-c].append(grid[r][c])
        for key in diags:
            if key>=0: #eloutani wel west
                diags[key].sort(reverse=True)
            else:
                diags[key].sort()
        for r in range(n):
            for c in range(n):
                grid[r][c]=diags[r-c].pop(0)
        return grid


        