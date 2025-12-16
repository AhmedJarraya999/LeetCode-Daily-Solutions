class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD=10**9+7
        #combinatroies solution
        seats=[]
        for i,c in enumerate(corridor):
            if c=="S":
                seats.append(i)
        l=len(seats)
        if l<2 or l%2==1:
            return 0
        res=1
        i=1
        while i <l-1: 
            res=(res*(seats[i+1]-seats[i]))%MOD
            i+=2
        return res



        # cache=[[-1]*3 for i in range(len(corridor))]#(i,sats)->count
        # def dfs(i,seats):
        #     if i==len(corridor):
        #         if seats==2:
        #             return 1
        #         else:
        #             return 0
        #     if cache[i][seats]!=-1:
        #         return cache[i][seats]
        #     res=0
        #     if seats==2:
        #         if corridor[i]=="S":
        #             res=dfs(i+1,1) #we set seats to 1 an not 0 since current is 1
        #         else:
        #             res=(dfs(i+1,0)+dfs(i+1,2))%MOD
        #     else:
        #         if corridor[i]=="S":
        #             res=dfs(i+1,seats+1)
        #         else:
        #             res=dfs(i+1,seats)
        #     cache[i][seats]=res
        #     return res
        # return dfs(0,0)
    

        