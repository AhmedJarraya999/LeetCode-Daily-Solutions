class Solution:
    def minimumDeletions(self, s: str) -> int:
        n=len(s)
        b_count_left=[0]*(n+1)
        a_count_right=[0]*(n+1)
        for i in range(1,len(s)+1):
            if s[i-1]=="b":
                b_count_left[i]=b_count_left[i-1]+1
            else:
                b_count_left[i]=b_count_left[i-1]
        for i in range(len(s)-2,-1,-1):
            if s[i+1]=="a":
                a_count_right[i]=a_count_right[i+1]+1
            else:
                a_count_right[i]=a_count_right[i+1]
        res=len(s)
        for i in range(len(s)):
            deletions=b_count_left[i]+a_count_right[i]
            res=min(res,deletions)
        return res
        
                


