from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(i, r, c, visited, word):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                    or board[r][c] != word[i] 
                    or (r, c) in visited):
                return False
            
            visited.add((r, c))
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if backtrack(i + 1, nr, nc, visited, word):
                    return True
            
            visited.remove((r, c))
            return False

        def exist(word: str) -> bool:
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == word[0] and backtrack(0, r, c, set(), word):
                        return True
            return False

        res = []
        for word in words:
            if exist(word):
                res.append(word)
        
        return res
