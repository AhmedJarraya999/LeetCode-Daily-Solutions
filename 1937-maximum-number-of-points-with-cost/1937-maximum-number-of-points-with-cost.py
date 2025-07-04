class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m=len(points)#rows
        n=len(points[0])#cols
        prev = points[0][:]
        for i in range(1,m):
            curr=[0]*n
            for j in range(n):
                max_val=float('-inf')
                for k in range(n):
                    cost=abs(j-k)
                    max_val=max(max_val,prev[k]-cost)
                curr[j]=max_val+points[i][j]
            prev=curr
        return max(prev)
       

        