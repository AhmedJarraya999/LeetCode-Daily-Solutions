from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        
        # 1. Build Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word   # store the word at the end node

        res = []

        def backtrack(r, c, parent):
            letter = board[r][c]
            currNode = parent[letter]

            # 2. Check if we found a word
            if "$" in currNode:
                res.append(currNode["$"])
                del currNode["$"]  # avoid duplicates

            # 3. Mark current cell as visited
            board[r][c] = "#"

            # 4. Explore neighbors
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    board[nr][nc] in currNode):
                    backtrack(nr, nc, currNode)

            # 5. Restore cell (backtracking)
            board[r][c] = letter

            # 6. Optimization: prune leaf nodes in Trie
            if not currNode:
                parent.pop(letter)

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    backtrack(r, c, trie)

        return res


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         rows = len(board)
#         cols = len(board[0])
        
#         def backtrack(i, r, c, visited, word):
#             if i == len(word):
#                 return True
#             if (r < 0 or r >= rows or c < 0 or c >= cols 
#                     or board[r][c] != word[i] 
#                     or (r, c) in visited):
#                 return False
            
#             visited.add((r, c))
#             directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc
#                 if backtrack(i + 1, nr, nc, visited, word):
#                     return True
            
#             visited.remove((r, c))
#             return False

#         # def exist(word: str) -> bool:
#         #     for r in range(rows):
#         #         for c in range(cols):
#         #             if board[r][c] == word[0] and backtrack(0, r, c, set(), word):
#         #                 return True
#         #     return False

#         res = []
#         for word in words:
#             found=False
#             for r in range(rows):
#                 for c in range(cols):
#                     if board[r][c]==word[0] and backtrack(0, r, c, set(), word):
#                         res.append(word)
#                         found=True
#                         break
#                     if found: break
#         return res
