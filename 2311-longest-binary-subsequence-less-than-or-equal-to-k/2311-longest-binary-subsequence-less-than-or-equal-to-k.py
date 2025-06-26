class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res=0
        cnt=0
        curSum=0
        for char in s[::-1]:
            if char=="0":
                res+=1
                cnt+=1
                curSum+=int(char)
            else:
                if curSum+2**cnt>k:
                    continue
                else:
                    curSum += 2 ** cnt
                    res+=1
                cnt+=1
        return res
                


        