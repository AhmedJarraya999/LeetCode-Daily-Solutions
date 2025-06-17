class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        visit=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        minHeap=[(0,0,0)] #diff,row,colum
        while minHeap:
            diff,r,c=heapq.heappop(minHeap)
            if (r,c) in visit:
                continure
            visit.add((r,c))

            #wselna lel target cell
            if (r,c)==(rows-1,cols-1):
                return diff
            for dr,dc in directions:
                newR,newC=r+dr,c+dc
                if newR<0 or newR==rows or newC<0  or newC==cols or (newR,newC) in visit:
                    continue
                newDiff=max(diff,abs(heights[r][c]-heights[newR][newC]))
                heapq.heappush(minHeap,[newDiff,newR,newC])



        