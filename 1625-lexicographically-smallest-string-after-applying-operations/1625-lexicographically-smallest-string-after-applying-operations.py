from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n=len(s)
        q=deque([s])
        visited=set()
        visited.add(s)
        res=s
        while q:
            curr=q.popleft()
            res=min(res,curr)
            o1=list(curr)
            #adding a to odd indicies
            for i in range(1,n,2):
                o1[i]=str((int(o1[i])+a)%10)
            o1="".join(o1)    
            if not o1 in visited:
                visited.add(o1)
                q.append(o1)
            #second rotation by transoframation
            o2=list(curr)
            o2=o2[-b:]+o2[:-b]
            o2="".join(o2)
            if o2 not in visited:
                visited.add(o2)
                q.append(o2)
        return res

