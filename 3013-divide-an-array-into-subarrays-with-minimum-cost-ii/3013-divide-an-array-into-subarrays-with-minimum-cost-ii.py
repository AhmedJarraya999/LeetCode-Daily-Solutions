class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        small=SortedList()
        large=SortedList()
        res=float('inf')
        n=len(nums)
        ##initial window
        for i in range(1,dist+2):
            small.add((nums[i],i))
        while len(small)>=k:
            s=small.pop(-1)
            large.add(s)
        curr=sum(s for s,_ in small)
        res=min(res,curr)
        for i in range(dist+2,n):
            pkey=(nums[i-dist-1],i-dist-1)
            nkey=(nums[i],i)
            ##remove left
            if pkey in small:
                small.discard(pkey)
                curr-=pkey[0]
                if large:
                    l=large.pop(0)
                    small.add(l)
                    curr+=l[0]
            elif pkey in large:
                large.discard(pkey)
            ##add right
            small.add(nkey)
            curr+=nkey[0]
            if len(small)>=k:
                s=small.pop(-1)
                large.add(s)
                curr-=s[0]
            res=min(res,curr)
        return nums[0]+res


        
        
      






        