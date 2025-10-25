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







