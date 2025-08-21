class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res=0
        n=len(mat)
        m=len(mat[0])
        heights = [0] * m
#Each bar’s height represents how many consecutive 1s we’ve seen in that column up to the current row.
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    heights[j]=0
                else:
                    heights[j]+=1
            stack=[]
            sum_ = [0] * m
            for j in range(m):
                # maintain monotonic increasing stack
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    sum_[j] = sum_[prev] + heights[j] * (j - prev)
                else:
                    sum_[j] = heights[j] * (j + 1)

                stack.append(j)
                res += sum_[j]
        return res



        