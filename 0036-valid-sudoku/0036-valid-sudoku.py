class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            n=len(board)
            rowset=set()
            colset=set()
            boxes=[set() for _ in range(9)]
            for row in range(n):
                for col in range(n):
                    if board[row][col]=='.':
                        continue
                    box_index=(col//3)+(row//3)*3
                    if board[row][col] in boxes[box_index]:
                        return False
                    else:
                        boxes[box_index].add(board[row][col])



            for row in range(n):
                rowset=set()
                for col in range(n):
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in rowset:
                        return False
                    rowset.add(board[row][col])
            for col in range(n):
                colset=set()
                for row in range(n):
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in colset:
                        return False    
                    colset.add(board[row][col]) 
            return True




            