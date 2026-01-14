class Solution:
    def residuePrefixes(self, s: str) -> int:
        ##OPTIMISED##
        seen=set()
        res=0
        for i,char in enumerate(s):
            seen.add(char)
            if len(seen)==((i+1)%3):
                res+=1
        return res
        # def checker(pref):
        #     if len(set(pref))==len(pref)%3:
        #         return True
        # pref=""
        # res=0
        # for char in s:
        #     pref+=char
        #     if checker(pref):
        #         res+=1
        # return res
        
        
        