class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        n = len(s)
    
        for c in set(s):  # unique characters in s
            first = s.find(c)
            last = s.rfind(c)
            
            if first < last:
                # characters between first and last occurrences
                middle_chars = set(s[first+1:last])
                result += len(middle_chars)
        
        return result