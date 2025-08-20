from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc = startPos
        hr, hc = homePos
        cost = 0
        
        # Move vertically
        if sr < hr:
            for r in range(sr + 1, hr + 1):
                cost += rowCosts[r]
        else:
            for r in range(sr - 1, hr - 1, -1):
                cost += rowCosts[r]
        
        # Move horizontally
        if sc < hc:
            for c in range(sc + 1, hc + 1):
                cost += colCosts[c]
        else:
            for c in range(sc - 1, hc - 1, -1):
                cost += colCosts[c]
        
        return cost
