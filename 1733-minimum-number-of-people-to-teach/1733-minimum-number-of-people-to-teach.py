from typing import List
class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        langs = [set(l) for l in languages]
        bad=set()
        for u,v in friendships:
            if  langs[u-1].isdisjoint(langs[v-1]): #no common 
                bad.add(u-1)
                bad.add(v-1)
        if not bad:
            return 0
        ans=float('inf')
        for l in range(1,n+1):
            need=0
            for person in bad:
                if l not in langs[person]:
                    need+=1
            ans=min(ans,need)
        return ans 








