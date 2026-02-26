from collections import defaultdict
import heapq
from typing import List
from math import inf

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=defaultdict(list)
        for o,c,w in zip(original,changed,cost):
            adj[o].append((c,w))
        lengths=sorted(set(len(o) for o in original))
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
                    heapq.heappush(heap,(cost+nw,nei))
            return dst 
        @cache 
        def dp(i):
            if i==len(source):
                return 0
            if source[i]==target[i]:
                best=dp(i+1)
            else:   best=inf
            for l in lengths:
                if i+l>len(source):
                    break
                s=source[i:i+l]
                t=target[i:i+l]
                dis=dijkstra(s)
                if t not in dis:
                    continue 
                best=min(best,dis[t]+dp(i+l))
            return best 
        res=dp(0)
        best = -1 if res==inf else res 


        return best





