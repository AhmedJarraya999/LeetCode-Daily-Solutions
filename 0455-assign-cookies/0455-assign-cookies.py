class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        j=0
        res=0
        for child in g:
            while j<len(s) and s[j]<child:
                j+=1
            if j<len(s):
                j+=1
                res+=1
        return res






        