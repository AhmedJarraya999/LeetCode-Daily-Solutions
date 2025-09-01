class Solution:
        def exist(self, board: List[List[str]], word: str) -> bool:
            rows=len(board)
            cols=len(board[0])
            def backtrack(i,r,c,visited):
                if i==len(word):
                    return True
                if (r < 0 or r >= rows or c < 0 or c >= cols 
                    or board[r][c] != word[i] 
                    or (r, c) in visited):
                    return False
                visited.add((r,c))

                res = (backtrack(i+1, r+1, c, visited) or
                    backtrack(i+1, r-1, c, visited) or
                    backtrack(i+1, r, c+1, visited) or
                    backtrack(i+1, r, c-1, visited))
                visited.remove((r, c))
                return res
            for r in range(rows):
                for c in range(cols):
                    if backtrack(0, r, c, set()):
                        return True
            return False
