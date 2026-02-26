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
        def dijkstra(s):
            heap=[(0,s)]
            dst={}
            while heap:
                cost,node=heapq.heappop(heap)
                if node in dst:
                    continue
                dst[node]=cost
                for nei,nw in adj[node]:
                    heapq.heappush(heap,(nw+cost,nei))
            return dst
        lengths=sorted(set(len(o) for o in original))
        @cache
        def dp(i):
            if i==len(source):
                return 0 #best case
            if source[i]==target[i]:
                best=dp(i+1)
            else: best=inf
            for l in lengths:
                if l+i>len(source):
                    break
                s=source[i:i+l]
                t=target[i:i+l]
                if s not in adj:
                    continue
                dis=dijkstra(s)
                if t not in dis:
                    continue
                best=min(best,dis[t]+dp(i+l))
            return best
        res=dp(0)
        return -1 if res == inf else res
                
        # adj=defaultdict(list)
        # for o,c,w in zip(original,changed,cost):
        #     adj[o].append((c,w))
        # lengths = sorted(set(len(o) for o in original))
        # def dijkstra(source):
        #     dst={}
        #     heap=[(0,source)]
        #     while heap:
        #         cost,node=heapq.heappop(heap)
        #         if node in dst:
        #             continue
        #         dst[node]=cost
        #         for nei,nw in adj[node]:
        #             heapq.heappush(heap,(cost+nw,nei))
        #     return dst
        # i=0
        # cost=0
        # while i<len(source):
        #     found=False
        #     for l in lengths:
        #         if i+l>len(source):
        #             continue
        #         s=source[i:i+l]
        #         t=target[i:i+l]
        #         if s==t:
        #             i+=l
        #             found=True
        #             break
        #         dis=dijkstra(s)
        #         if t in dis:
        #             cost+=dis[t]
        #             i+=l
        #             found=True
        #             break
        #     if not found:return -1
        # return cost





















                    
        
        # adj = defaultdict(list)
        # for o, c, w in zip(original, changed, cost):
        #     adj[o].append((c, w))
        
        # def dijkstra(start):
        #     dist = {}
        #     heap = [(0, start)]
            
        #     while heap:
        #         curr_cost, node = heapq.heappop(heap)
        #         if node in dist:
        #             continue
        #         dist[node] = curr_cost
                
        #         for nei, w in adj[node]:
        #             heapq.heappush(heap, (curr_cost + w, nei))
            
        #     return dist
        
        # # 🔥 collect all possible transformation lengths
        # lengths = set(len(o) for o in original)
        
        # total_cost = 0
        # n = len(source)
        
        # i = 0
        # while i < n:
            
        #     found = False
            
        #     for L in lengths:
        #         if i + L > n:
        #             continue
                
        #         s = source[i:i+L]
        #         t = target[i:i+L]
                
        #         if s == t:
        #             i += L
        #             found = True
        #             break
                
        #         dis = dijkstra(s)
                
        #         if t in dis:
        #             total_cost += dis[t]
        #             i += L
        #             found = True
        #             break
            
        #     if not found:
        #         return -1
        
        # return total_cost
        