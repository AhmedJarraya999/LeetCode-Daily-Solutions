class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        cached_disjktra={}
        adj=defaultdict(list)
        for o,c,w in zip(original,changed,cost):
            adj[o].append((c,w))
        def disjktra(source):
            heap=[(0,source)]
            dist={}
            while heap:
                cost,node=heapq.heappop(heap)
                if node in dist:
                    continue
                dist[node]=cost
                for nei,nw in adj[node]:
                    heapq.heappush(heap,(nw+cost,nei))
            return dist
        cost=0
        for s,t in zip(source,target):
            if s==t:
                continue
            if s not in cached_disjktra:
                sp_f_s=disjktra(s)
                cached_disjktra[s]=sp_f_s
            if t not in cached_disjktra[s]:
                return -1
            cost+=cached_disjktra[s][t]
        return cost 
            
        













        # adj=defaultdict(list)
        # for o,c,w in zip(original,changed,cost):
        #     adj[o].append((c,w))
        # shortest_path_source={}
        # def disjktra(source):
        #     dst={}
        #     heap=[(0,source)]
        #     while heap:
        #         cost,node=heapq.heappop(heap)
        #         if node in dst:
        #             continue
        #         dst[node]=cost
        #         for nei,nc in adj[node]:
        #             heapq.heappush(heap,(nc+cost,nei))
        #     return dst
        # res=0
        # for s,t in zip(source,target):
        #     if s==t:
        #         continue
        #     if s not in shortest_path_source:
        #         shortest_path_source[s]=disjktra(s)
        #     if t  not in shortest_path_source[s]:
        #         return -1
        #     res+=shortest_path_source[s][t]
        # return res






        # shortest_path = {}
        # adj = defaultdict(list)

        # for o, c, w in zip(original, changed, cost):
        #     adj[o].append((c, w))

        # def dijkstra(start):
        #     heap = [(0, start)]
        #     min_cost_map = {}

        #     while heap:
        #         curr_cost, node = heapq.heappop(heap)

        #         if node in min_cost_map:
        #             continue

        #         min_cost_map[node] = curr_cost

        #         for nei, w in adj[node]:
        #             heapq.heappush(heap, (curr_cost + w, nei))

        #     return min_cost_map

        # res = 0

        # for s, t in zip(source, target):
        #     if s == t:
        #         continue

        #     if s not in shortest_path:
        #         shortest_path[s] = dijkstra(s)

        #     min_cost = shortest_path[s].get(t, float('inf'))

        #     if min_cost == float('inf'):
        #         return -1

        #     res += min_cost

        # return res
# class Solution:
#     def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
#         shortest_path={}
#         adj=defaultdict(list)
#         for o,c,w in zip(original,changed,cost):
#             adj[o].append((c,w))
#         def disjktra(source):
#             heap=[(0,source)]
#             min_cost_map={}
#             while heap:
#                 cost,node=heapq.heappop(heap)
#                 if node in min_cost_map:
#                     continue
#                 min_cost_map[node]=cost
#                 for nei,nei_cost in adj[node]:
#                     heapq.heappush(heap,(cost+nei_cost,nei))
#             return min_cost_map
#         res=0
#         for s,t in zip(source,target):
#             if s not in shortest_path:
#                 shortest_path[s]=disjktra(s)
#             min_cost=shortest_path[s][t]
#             if min_cost == float('inf'):
#                 return -1
#             res+=min_cost
#         return res







        # graph=defaultdict(list)
        # for o,c,w in zip(original,changed,cost):
        #     u = ord(o) - ord('a')
        #     v = ord(c) - ord('a')
        #     graph[u].append((v,w))


        # shortest_cache = {}
        # def dijkstra(start):
        #     dist = [float('inf')] * 26
        #     dist[start] = 0
        #     pq = [(0, start)]
        #     while pq:
        #         curr_cost,node=heapq.heappop(pq)
        #         if curr_cost > dist[node]:
        #             continue
                
        #         for neighbor, weight in graph[node]:
        #             new_cost = curr_cost + weight
        #             if new_cost < dist[neighbor]:
        #                 dist[neighbor] = new_cost
        #                 heapq.heappush(pq, (new_cost, neighbor))
            
        #     return dist
        # total = 0
        
        # for s, t in zip(source, target):
        #     if s == t:
        #         continue
            
        #     u = ord(s) - ord('a')
        #     v = ord(t) - ord('a')
            
        #     # Run Dijkstra only once per start node
        #     if u not in shortest_cache:
        #         shortest_cache[u] = dijkstra(u)
            
        #     min_cost = shortest_cache[u][v]
            
        #     if min_cost == float('inf'):
        #         return -1
            
        #     total += min_cost
        
        # return total