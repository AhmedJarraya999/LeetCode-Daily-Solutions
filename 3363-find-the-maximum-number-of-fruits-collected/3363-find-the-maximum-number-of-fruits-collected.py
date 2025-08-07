class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        INF = float('inf')


        # 1) Sum of main diagonal
        first = sum(fruits[i][i] for i in range(n))

        # Helper DFS with memoization
        def make_dfs(dirs):
            @lru_cache(None)
            def dfs(r: int, c: int, moves: int) -> int:
                # Reached bottom-right?
                if r == n - 1 and c == n - 1:
                    return 0 if moves == 0 else INF
                # No moves left or on main diagonal
                if moves == 0 or r == c:
                    return INF

                best = -1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        val = dfs(nr, nc, moves - 1)
                        if val != INF:
                            best = max(best, val)
                return INF if best < 0 else fruits[r][c] + best
            return dfs

        # 2) Second path: from top-right to bottom-right
        down_dirs = [(1, -1), (1, 0), (1, 1)]
        dfs_down = make_dfs(down_dirs)
        second = dfs_down(0, n - 1, n - 1)

        # 3) Third path: from bottom-left to bottom-right
        right_dirs = [(-1, 1), (0, 1), (1, 1)]
        dfs_right = make_dfs(right_dirs)
        third = dfs_right(n - 1, 0, n - 1)

        return first + second + third
