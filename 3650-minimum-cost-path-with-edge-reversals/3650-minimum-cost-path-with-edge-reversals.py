class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist=[0]+[inf]*(n-1)
        adj=defaultdict(list)
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w*2))
        visited=set()
        heap=[(0,0)]
        while heap:
            w,node=heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for nei,nw in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,(w+nw,nei))
                # if w > dist[node]:
                #     continue   # ← this replaces visited
                if w+nw<dist[nei]:
                    dist[nei] = w + nw
        return dist[n - 1] if dist[n - 1] != inf else -1


        ###understand in context of dense graph why it is better to use  a set checker
        ###understand

        









        # adj=defaultdict(list)
        # for a,b,w in edges:
        #     adj[a].append((b,w))
        #     adj[b].append((a,w*2))
        # heap=[(0,0)]
        # dist = [0] + [inf] * (n - 1)
        # while heap:
        #     w,node=heapq.heappop(heap)
        #     for nei,nw in adj[node]:
        #         if w+nw<dist[nei]:
        #             dist[nei] = w + nw
        #         heapq.heappush(heap,(w+nw,nei))
        # return dist[n - 1] if dist[n - 1] != inf else -1
        



























        # adj = defaultdict(list)
        # for a, b, w in edges:
        #     adj[a].append((b, w))
        #     adj[b].append((a, w * 2))
        # dist = [0] + [inf] * (n - 1)
        # heap = []
        # heapq.heappush(heap, (0, 0))
        # while heap:
        #     w, node = heapq.heappop(heap)
        #     for nei, nw in adj[node]:
        #         if w + nw < dist[nei]:
        #             dist[nei] = w + nw
        #             heapq.heappush(heap, (w + nw, nei))
        # return dist[n - 1] if dist[n - 1] != inf else -1
        # adj={}
        # shortest={}
        # for src,dst,weight in adj:
        #     adj[src].append(dst,weight)
        # minHeap=[[0,src]]
        # while minHeap:
        #     w1,n1=heapq.heappop(minHeap)
        #     if n1 not in shortest:
        #         continue
        #     shortest[n1]=w1
        #     for n2,w2 in adj[n1]:
        #         heapq.heappush(minHeap,(W1,+w2,n2))
        # if n-1 in shortest:
        #     return shortest[n-1]
        # else:
        #     return -1
