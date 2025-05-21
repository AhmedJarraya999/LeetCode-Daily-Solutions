class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
    
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows and columns that need to be zeroed
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
            