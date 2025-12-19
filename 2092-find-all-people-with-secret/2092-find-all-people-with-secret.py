from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        # Step 1: Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        # Step 2: Initialize who knows the secret
        knows = {0, firstPerson}
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            # Collect all meetings at the same time
            same_time = []
            while i < len(meetings) and meetings[i][2] == time:
                same_time.append(meetings[i])
                i += 1
            
            # Build a graph for this time group
            graph = defaultdict(list)
            for x, y, _ in same_time:
                graph[x].append(y)
                graph[y].append(x)
            
            # BFS/DFS to spread secret among connected components
            visited = set()
            def dfs(node, component):
                visited.add(node)
                component.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        dfs(nei, component)
            
            # For each connected component, check if someone knows secret
            for person in graph:
                if person not in visited:
                    component = set()
                    dfs(person, component)
                    if component & knows:  # intersection not empty
                        knows |= component  # everyone learns the secret
        
        return list(knows)
