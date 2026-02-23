class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=defaultdict(list)
        cached_disjkstra={}
        for o,c,w in zip(original,changed,cost):
            adj[o].append((c,w))
        def dijkstra(source):
            dst={}
            heap=[(0,source)]
            while heap:
                cost,node=heapq.heappop(heap)
                if node in dst:
                    continue
                dst[node]=cost
                for nei,nw in adj[node]:
                    heapq.heappush(heap,(nw+cost,nei))
            return dst
        cost=0
        for s,t in zip(source,target):
            if s==t:
                continue
            if s not in cached_disjkstra:
                dis=dijkstra(s)
                cached_disjkstra[s]=dis
            if t not in cached_disjkstra[s]:
                return -1
            cost+=cached_disjkstra[s][t]
        return cost

        