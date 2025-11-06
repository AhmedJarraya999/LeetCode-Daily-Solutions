from typing import List
from sortedcontainers import SortedSet

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        
        # Step 1: Union all connected stations into components
        for u, v in connections:
            uf.union(u, v)
        
        # Step 2: Build a map root -> sorted set of online stations
        online_stations = {}
        for i in range(1, c + 1):
            root = uf.find(i)
            if root not in online_stations:
                online_stations[root] = SortedSet()
            online_stations[root].add(i)
        
        # All stations are initially online
        online = [True] * (c + 1)
        results = []

        # Step 3: Process queries
        for qtype, x in queries:
            root = uf.find(x)
            if qtype == 1:  # maintenance check
                if online[x]:
                    results.append(x)
                else:
                    stations = online_stations.get(root, SortedSet())
                    if len(stations) == 0:
                        results.append(-1)
                    else:
                        results.append(stations[0])  # smallest online station
            else:  # qtype == 2: take offline
                if online[x]:
                    online[x] = False
                    online_stations[root].discard(x)
        
        return results
