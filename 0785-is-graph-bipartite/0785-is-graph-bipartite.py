class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd=[0]*len(graph) #Map node i -> odd=1,even=-1
        def bfs(i):
            if odd[i]:
                return True #visited yaani soit 1 ou -1
            q=deque([i])
            odd[i]=-1
            while q:
                i=q.popleft()
                for nei in graph[i]:
                    if odd[i]==odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei]=-1 *odd[i]
            return True
        #loop for every node because graph might be not connected
        for i in range(len(graph)):
            if  not bfs(i):
                return False
        return True

        