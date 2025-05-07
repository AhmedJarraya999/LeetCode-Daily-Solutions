class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
        res=0
        visited=set()
        for i in range(len(isConnected)):
            if i not in visited:
                res+=1
                dfs(i)
        return res
        