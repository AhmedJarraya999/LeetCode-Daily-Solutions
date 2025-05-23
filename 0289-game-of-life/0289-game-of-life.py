class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows,cols=len(board),len(board[0])
        copy_board=deepcopy(board)
        def count_live_neighbours(r,c):
            directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            live_neighbours=0
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and copy_board[nr][nc]==1:
                    live_neighbours+=1
            return live_neighbours
        for r in range(rows):
            for c in range(cols):
                live_neighbours=count_live_neighbours(r,c)
                if copy_board[r][c] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[r][c] = 0
                elif copy_board[r][c] == 0 and live_neighbours == 3:
                    board[r][c] = 1


        