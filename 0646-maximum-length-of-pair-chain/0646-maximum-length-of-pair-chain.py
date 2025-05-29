class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res=0
        curr_end=float('-inf')
        pairs.sort(key=lambda p:p[1])
        for start,end in pairs:
            if start>curr_end:
                res+=1
                curr_end=end    
        return res

        