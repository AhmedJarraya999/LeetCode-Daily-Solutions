class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N=len(grid)
        count=defaultdict(int) #by default initiation to zero
        for i in range(N):
            for j in range(N):
                count[grid[i][j]]+=1
        double,missing=0,0
        for num in range(1,N*N+1):
            if count[num]==0:
                missing=num
            if count[num]==2:
                double=num
        return [double,missing]
