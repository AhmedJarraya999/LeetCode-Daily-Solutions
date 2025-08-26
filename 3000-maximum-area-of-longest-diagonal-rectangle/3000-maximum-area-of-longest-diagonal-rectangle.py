class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n=len(dimensions)
        maxdiag=float('-inf')
        maxarea=float('-inf')
        for area,length in dimensions:
            diag=sqrt(area*area+length*length)
            areaval=area*length
            if diag>maxdiag:
                maxdiag=diag
                maxarea=areaval
            elif diag==maxdiag:
                maxarea=max(maxarea,areaval)
        return maxarea




