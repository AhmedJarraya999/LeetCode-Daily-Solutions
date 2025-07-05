class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        visited = set([1])
        factors = [2, 3, 5]

        for _ in range(n):
            num = heapq.heappop(minHeap)
            for f in factors:
                next_ugly = num * f
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(minHeap, next_ugly)
        return num