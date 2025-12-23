from typing import List
from functools import lru_cache

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols=len(strs[0])
        rows=len(strs)
        dp=[1]*cols
        for c1 in range(cols-2,-1,-1):
            for c2 in range(c1+1,cols):
                valid=True
                for row in range(rows):
                    if strs[row][c1]>strs[row][c2]:
                        valid=False
                        break
                if valid:
                    dp[c1]=max(dp[c1],1+dp[c2])
        return cols-max(dp)
      