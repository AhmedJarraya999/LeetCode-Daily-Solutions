from typing import List

class Solution:
    def maximizeSquareArea(
        self, 
        m: int, 
        n: int, 
        hFences: List[int], 
        vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        # Add boundaries
        hFences += [1, m]
        vFences += [1, n]

        hFences.sort()
        vFences.sort()

        # All possible horizontal distances
        hd = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hd.add(hFences[j] - hFences[i])

        # All possible vertical distances
        vd = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                vd.add(vFences[j] - vFences[i])

        # Find maximum common distance
        common = hd & vd
        if not common:
            return -1

        max_side = max(common)
        return (max_side * max_side) % MOD
