class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph=defaultdict(list)
        for o,c,w in zip(original,changed,cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            graph[u].append((v,w))


        shortest_cache = {}
        def dijkstra(start):
            dist = [float('inf')] * 26
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                curr_cost,node=heapq.heappop(pq)
                if curr_cost > dist[node]:
                    continue
                
                for neighbor, weight in graph[node]:
                    new_cost = curr_cost + weight
                    if new_cost < dist[neighbor]:
                        dist[neighbor] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor))
            
            return dist
        total = 0
        
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            
            # Run Dijkstra only once per start node
            if u not in shortest_cache:
                shortest_cache[u] = dijkstra(u)
            
            min_cost = shortest_cache[u][v]
            
            if min_cost == float('inf'):
                return -1
            
            total += min_cost
        
        return total