class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adjacency list
        
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))  # (neighbor, weight)


        pq = [(0, k)]
        visited = set()
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            dist[node] = time

            for nei, w in graph[node]:
                if nei not in visited:
                    heapq.heappush(pq, (time + w, nei))

        # If not all nodes are visited, return -1
        if len(dist) != n:
            return -1

        return max(dist.values())