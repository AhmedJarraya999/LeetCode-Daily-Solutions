class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        myset=defaultdict(int)
        for ch in s:
            myset[ch]+=1
        myset2=defaultdict(int)
        for c in t:
            myset2[c]+=1
        for el in myset2:
            if myset2[el]!=myset[el] or el not in myset:
                return el

        