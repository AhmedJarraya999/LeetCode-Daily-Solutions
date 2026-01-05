class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        countneg=0
        lowestelement=float('inf')
        res=0
        for row in matrix:
            for val in row:
                if val<0:
                    countneg+=1
        if countneg%2==0:
            for row in matrix:
                for val in row:
                    res+=abs(val)
            return res
        if countneg%2==1:
            for row in matrix:
                for val in row:
                    res+=abs(val)
                    lowestelement=min(abs(val),lowestelement)
            return res-2*lowestelement 
            ##2 multiplication observation trick




        