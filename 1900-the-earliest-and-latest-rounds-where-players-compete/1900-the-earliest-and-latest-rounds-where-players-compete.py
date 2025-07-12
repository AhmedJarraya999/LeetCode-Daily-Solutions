from typing import List
from functools import cache
from itertools import product

class Solution:
    def earliestAndLatest(self, n: int, f: int, s: int) -> List[int]:
        self.res = set()

        @cache
        def dfs(players, round):
            n = len(players)
            pairs = []

            for i in range(n // 2):
                a = players[i]
                b = players[n - 1 - i]

                if a == f and b == s:
                    self.res.add(round)
                    return

                if a not in (f, s) and b not in (f, s):
                    pairs.append((a, b))

            # If odd number of players, middle player goes to next round
            to_add = (f, s) if n % 2 == 0 else tuple(set((f, s, players[n // 2])))

            for winners in product(*pairs):
                next_players = sorted(winners + to_add)
                dfs(tuple(next_players), round + 1)

        dfs(tuple(range(1, n + 1)), 1)
        return [min(self.res), max(self.res)]
