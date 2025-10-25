class Solution:
    def totalMoney(self, n: int) -> int:
        day=0
        res=0
        start=1
        while day<n:
            cur=start
            for i in range(7):
                if day==n:
                    break
                res+=cur
                cur+=1
                day+=1
            start+=1
        return res










        startingpoint=0
        res=0
        addition=1
        checker=0
        for d in range(n):
            while checker<7:
                res+=startingpoint+addition
                checker+=1
            checker=0
            startingpoint+=1
            res+=startingpoint+addition
        return res

        