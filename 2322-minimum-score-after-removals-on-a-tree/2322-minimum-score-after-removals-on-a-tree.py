from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)

        # Build adjacency list for the tree
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        xor = [0] * n

        # DFS to compute XOR of subtree rooted at each node
        def xor_dfs(node, par):
            curr = nums[node]
            for nei in adj[node]:
                if nei != par:
                    curr ^= xor_dfs(nei, node)
            xor[node] = curr
            return curr

        xor_dfs(0, -1)

        # DFS to collect all nodes in each subtree
        subtree_nodes = [set() for _ in range(n)]
        def subtree_nodes_dfs(node, par):
            curr = set([node])
            for nei in adj[node]:
                if nei != par:
                    curr |= subtree_nodes_dfs(nei, node)
            subtree_nodes[node] = curr
            return curr

        subtree_nodes_dfs(0, -1)

        res = float('inf')

        # Try all combinations of two removed edges (i, j)
        for i in range(1, n):
            for j in range(i + 1, n):
                # Check relationships between the subtrees of node i and j
                if j in subtree_nodes[i]:
                    a = xor[j]
                    b = xor[i] ^ xor[j]
                    c = xor[0] ^ xor[i]
                elif i in subtree_nodes[j]:
                    a = xor[i]
                    b = xor[j] ^ xor[i]
                    c = xor[0] ^ xor[j]
                else:
                    a = xor[i]
                    b = xor[j]
                    c = xor[0] ^ xor[i] ^ xor[j]

                res = min(res, max(a, b, c) - min(a, b, c))

        return res
