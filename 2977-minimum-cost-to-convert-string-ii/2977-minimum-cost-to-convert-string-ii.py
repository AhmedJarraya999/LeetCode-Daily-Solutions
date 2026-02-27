from collections import defaultdict
import heapq
from typing import List
from math import inf
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=defaultdict(list)
        for o,c,w in zip(original,changed,cost):
            adj[o].append((c,w))
        @cache
        def dijkstra(source):
            heap=[(0,source)]
            dst={}
            while heap:
                cost,node=heapq.heappop(heap)
                if node in dst:
                    continue
                dst[node]=cost
                for nei,nw in adj[node]:
                    heapq.heappush(heap,(nw+cost,nei))
            return dst

        lengths=set(len(o) for o in original)
        @cache
        def dp(i):
            if i==len(source):
                return 0
            if source[i]==target[i]:
                res=dp(i+1)
            else:
                res=inf 
            for l in sorted(lengths):
                if i+l>len(source):
                    break
                s=source[i:i+l]
                t=target[i:i+l]
                if s not in adj:
                    continue
                dis=dijkstra(s)
                if t not in dis:
                    continue
                dis=dis[t]
                res=min(res,dis+dp(i+l))
            return res
        res=dp(0)
        if res==inf:
            return -1
        else:
            return res
        

        
        

            
        
        
        
                
        



