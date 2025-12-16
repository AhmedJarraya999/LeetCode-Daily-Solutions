class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD=10**9+7
        cache=[[-1]*3 for i in range(len(corridor))]#(i,sats)->count
        def dfs(i,seats):
            if i==len(corridor):
                if seats==2:
                    return 1
                else:
                    return 0
            if cache[i][seats]!=-1:
                return cache[i][seats]
            res=0
            if seats==2:
                if corridor[i]=="S":
                    res=dfs(i+1,1) #we set seats to 1 an not 0 since current is 1
                else:
                    res=(dfs(i+1,0)+dfs(i+1,2))%MOD
            else:
                if corridor[i]=="S":
                    res=dfs(i+1,seats+1)
                else:
                    res=dfs(i+1,seats)
            cache[i][seats]=res
            return res
        return dfs(0,0)
        # nb=0
        # for c in corridor:
        #     if c=="S":
        #         nb+=1
        # if nb<2:
        #     return 0%MOD
        # if nb<4:
        #     return 1%MOD
        # seat_count=0
        # segments=[]
        # start_index =0
        # for i,c in enumerate(corridor):
        #     if c=="S":
        #         seat_count+=1
        #         if seat_count==1:
        #             start_index=i
        #         elif seat_count==2:
        #             segments.append(corridor[start_index:i+1])
        #             seat_count=0


        

        