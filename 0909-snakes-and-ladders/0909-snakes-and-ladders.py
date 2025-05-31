class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l=len(board)
        board.reverse()
        def intToPos(square):
            r=(square-1)//l
            c=(square-1)%l
            if r%2:
                c=l-1-c
            return [r,c]
        q=deque()  #squares,moves
        q.append([1,0])
        visit=set()
        while q:
            square,moves=q.popleft()
            for i in range(1,7):
                nextSquare=square+i
                r,c=intToPos(nextSquare)
                if board[r][c]!=-1:
                    nextSquare=board[r][c]
                if nextSquare==l*l:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare,moves+1])
        return -1
            



        