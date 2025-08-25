class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        direction=1
        m=len(matrix)
        n=len(matrix[0])
        result=[]
        row=0
        col=0
        for _ in range(m*n):
            result.append(matrix[row][col])
            if direction==1:#tal3in fouk ymin
                if col==n-1:
                    row+=1
                    direction=-1
                elif row==0:
                    col+=1
                    direction=-1
                else:
                    row-=1
                    col+=1
            else: #louta habtin
                if row==m-1:
                    col+=1
                    direction=1
                elif col==0:
                    row+=1
                    direction=1
                else:
                    row+=1
                    col-=1
        return result