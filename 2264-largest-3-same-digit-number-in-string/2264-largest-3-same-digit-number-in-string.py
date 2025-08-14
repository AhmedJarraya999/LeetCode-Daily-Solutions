class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=""
        for i  in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                candidate=num[i]*3
                if res=="" or candidate>res :
                    res=candidate
        return res
        