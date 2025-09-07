class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=len(a)
        y=len(b)
        bigger=max(x,y)
        parts=[]
        carry=0
        for i in range(bigger):
            bit_a=int(a[x-1-i]) if i<x else 0
            bit_b=int(b[y-1-i]) if i<y else 0
            tot=bit_a+bit_b+carry
            parts.insert(0,str(tot%2))
            carry=tot//2
        if carry:
            parts.insert(0,"1")
        return "".join(parts)