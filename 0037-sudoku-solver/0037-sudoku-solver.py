class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(r, c, ch):
            # Check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            # Check column
            for i in range(9):
                if board[i][c] == ch:
                    return False
            # Check 3x3 subgrid
            startRow, startCol = 3 * (r // 3), 3 * (c // 3)
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str, range(1, 10)):
                            if isValid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False  # if no number fits
            return True  # solved

        backtrack()
