class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards=set(map(tuple,guards))
        walls=set(map(tuple,walls)) #transform into tuple to make them hashable
        guarded=set()
        tot_cells=m*n
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for gr,gc in guards:
            for dr,dc in directions:
                nr=gr+dr
                nc=gc+dc
                while 0<=nr<m and 0<=nc<n and (nr,nc) not in walls and (nr,nc) not in guards:
                    guarded.add((nr,nc))
                    nr+=dr
                    nc+=dc
        return tot_cells-len(guards)-len(walls)-len(guarded)

        # guards=set(guards)
        # walls=set(walls)
        # for r in range(m):
        #     for j in rang(n):
        #         if [r,j] in walls:
        #             continue
        #         if [r,j] in guards:
        #             continue
        #         else:
        #             directions=[(-1,0),(1,0),(0,1),(0,-1)]
        #             for dr,dc in directions:
        #                 nr=r+dr
        #                 nc=c+dc
                    
        