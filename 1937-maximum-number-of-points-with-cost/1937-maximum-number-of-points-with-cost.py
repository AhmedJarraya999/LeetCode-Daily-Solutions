class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # m=len(points)#rows
        # n=len(points[0])#cols
        # prev = points[0][:]
        # for i in range(1,m):
        #     curr=[0]*n
        #     for j in range(n):
        #         max_val=float('-inf')
        #         for k in range(n):
        #             cost=abs(j-k)
        #             max_val=max(max_val,prev[k]-cost)
        #         curr[j]=max_val+points[i][j]
        #     prev=curr
        # return max(prev)

        
        m, n = len(points), len(points[0])
        prev = points[0][:]  # initialize with the first row
        
        for i in range(1, m):
            left = [0] * n
            right = [0] * n
            curr = [0] * n
            
            # Left to right pass
            left[0] = prev[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, prev[j])
            
            # Right to left pass
            right[n - 1] = prev[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev[j])
            
            # Compute max for each column
            for j in range(n):
                curr[j] = points[i][j] + max(left[j], right[j])
            
            prev = curr  # update for next row
        
        return max(prev)
       

        