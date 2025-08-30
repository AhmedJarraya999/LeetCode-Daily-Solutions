from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Step 0: Assign unique group ids to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Step 1: Build graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for i in range(n):
            for before in beforeItems[i]:
                item_graph[before].append(i)
                item_indegree[i] += 1
                if group[i] != group[before]:
                    group_graph[group[before]].append(group[i])
                    group_indegree[group[i]] += 1

        # Topological sort function
        def topo_sort(graph, indegree, nodes):
            res = []
            queue = deque([node for node in nodes if indegree[node] == 0])
            while queue:
                u = queue.popleft()
                res.append(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            return res if len(res) == len(nodes) else []

        # Step 2: Topo sort all items globally
        items_sorted = topo_sort(item_graph, item_indegree, list(range(n)))
        if not items_sorted:
            return []

        # Step 3: Group items according to their group in the sorted order
        group_to_items = defaultdict(list)
        for item in items_sorted:
            group_to_items[group[item]].append(item)

        # Step 4: Topo sort groups
        groups_sorted = topo_sort(group_graph, group_indegree, list(range(m)))
        if not groups_sorted:
            return []

        # Step 5: Combine items according to sorted groups
        result = []
        for g in groups_sorted:
            result.extend(group_to_items[g])
        return result
