class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(k):
            removed=[False]*len(s)
            for i in range(k):
                removed[removable[i]]=True
            j=0
            for i in range(len(s)):
                if not removed[i] and s[i]==p[j]:
                    j+=1
                    if j==len(p):
                        return True
            return j==len(p)
        left,right=0,len(removable)
        ans=0
        while left<=right:
            mid=(left+right)//2
            if isSubseq(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans























###Brute foooorce

        # def isSubsequence(s:str, p:str):
        #     i,j=0,0
        #     while i<len(p) and j<len(s):
        #         if s[j]==p[i]:
        #             i+=1
        #         j+=1
        #     return i==len(p)
        # for k in range(len(removable)+1):
        #     removed=set(removable[:k])
        #     new_s="".join([c for i,c in enumerate(s) if i not in removed ])
        #     if not isSubsequence(new_s,p):
        #         return k-1
        # return len(removable)


