class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        nbdeleted=0
        for c in range(cols):
            for r in range(rows-1):
                if strs[r][c]>strs[r+1][c]:
                    nbdeleted+=1
                    break
        return nbdeleted
