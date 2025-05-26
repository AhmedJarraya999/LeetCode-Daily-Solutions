class Solution:
    def largestPathValue(self,colors: str, edges: list[list[int]]) -> int:
        adj=defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
        #return max frequent color for each node
        def dfs(node):
            if node in path:
                return float('inf')
            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorIndex=ord(colors[node]) - ord('a')
            count[node][colorIndex]=1
            for nei in adj[node]:
                if dfs(nei)==float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c]=max(
                        count[node][c],
                        (1 if c==colorIndex else 0)+ count[nei][c]
                    )
            path.remove(node)
            return max(count[node])
        visit,path=set(),set()
        n=len(colors)
        count=[[0]*26 for i in range(n)]#map counter for each color
        n,res=len(colors),0
        for i in range(n):
            res=max(dfs(i),res)
        return res if res!=float('inf') else -1
