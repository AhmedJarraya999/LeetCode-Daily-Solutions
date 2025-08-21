from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        res = 0

        # Step 1: build row-wise prefix of consecutive 1s
        # left[i][j] = number of consecutive 1s ending at (i,j) in the row
        left = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    left[i][j] = (left[i][j-1] if j > 0 else 0) + 1

        # Step 2: for each (i,j), go upward and accumulate
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                # width of rectangle is limited by minimum width of consecutive 1s
                width = left[i][j]
                # move upward
                for k in range(i, -1, -1):
                    width = min(width, left[k][j])
                    if width == 0:
                        break
                    res += width

        return res
