class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        left=set()
        right=Counter(s)
        for mid in s:
            right[mid]-=1
            for c in left:
                if right[c]>0:
                    res.add((mid,c))
            left.add(mid)
        return len(res)








        # result = 0
        # n = len(s)
    
        # for c in set(s):  # unique characters in s
        #     first = s.find(c)
        #     last = s.rfind(c)
            
        #     if first < last:
        #         # characters between first and last occurrences
        #         middle_chars = set(s[first+1:last])
        #         result += len(middle_chars)
        
        # return result