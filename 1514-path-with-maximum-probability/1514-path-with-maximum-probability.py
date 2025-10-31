class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph=defaultdict(list)
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        # Max-heap: store (-probability, node) because heapq is min-heap by default
        heap = [(-1.0, start)]
        best=[0.0] * n
        best[start]=1.0
        while heap:
            prob,node=heapq.heappop(heap)
            prob = -prob
            if node == end:
                return prob 
            for neighbor, p in graph[node]:
                new_prob = prob * p
                if new_prob > best[neighbor]:
                    best[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        return 0.0

        