class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=n*m-1
        while left<=right:
            mid=(left+right)//2
            row=mid//m #do not forget starting from zero
            col=mid%m
            mid_val=matrix[row][col]
            if mid_val==target:
                return True
            elif mid_val<target:
                left=mid+1
            else:
                right=mid-1
        return False



        