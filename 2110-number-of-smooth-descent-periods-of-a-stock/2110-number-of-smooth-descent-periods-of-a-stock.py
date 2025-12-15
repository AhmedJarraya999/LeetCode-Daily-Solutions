class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=len(prices)
        dp=1
        total=1
        for i in range(1,n):
            if prices[i]==prices[i-1]-1:
                dp+=1
            else:
                dp=1
            total+=dp
        return total