class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for i in range(n):
            freq = [0] * 26
            
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                
                # Check if current substring is balanced
                count = 0
                distinct = 0
                
                for f in freq:
                    if f > 0:
                        distinct += 1
                        if count == 0:
                            count = f
                        elif count != f:
                            break
                else:
                    # only executes if loop didn't break
                    res = max(res, j - i + 1)
                    
        return res
