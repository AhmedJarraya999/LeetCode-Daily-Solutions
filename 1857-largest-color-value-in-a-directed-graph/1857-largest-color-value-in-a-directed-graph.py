class Solution:
    def largestPathValue(self,colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        queue = deque()
        
        # Start with all nodes having zero indegree
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        max_color_value = 0

        while queue:
            u = queue.popleft()
            visited += 1
            color_index = ord(colors[u]) - ord('a')
            dp[u][color_index] += 1
            max_color_value = max(max_color_value, dp[u][color_index])

            for v in graph[u]:
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return max_color_value if visited == n else -1
