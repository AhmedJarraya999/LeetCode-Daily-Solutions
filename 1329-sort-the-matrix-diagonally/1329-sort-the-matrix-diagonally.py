class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        diags=defaultdict(list)
        for r in range(n):
            for c in range(m):
                diags[r-c].append(mat[r][c])
        for key in diags:
            diags[key].sort(reverse=True)
        for r in range(n):
            for c in range(m):
                mat[r][c]=diags[r-c].pop()
        return mat