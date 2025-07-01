class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)
        groups=[]
        i=0
        while i<n:
            j=i
            while j<n and word[j]==word[i]:
                j+=1
            groups.append(word[i:j])
            i=j
        count=1
        for g in groups: 
            if len(g)>=2:
                count+=len(g)-1
        return count
        