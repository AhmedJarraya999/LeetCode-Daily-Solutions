class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))
        
        # Maximize: replace first non-9 digit with 9
        for ch in s:
            if ch != '9':
                max_s = ''.join(['9' if c == ch else c for c in s])
                break
        else:
            max_s = ''.join(s)
        
        # Minimize
        if s[0] != '1':
            min_s = ''.join(['1' if c == s[0] else c for c in s])
        else:
            for i in range(1, len(s)):
                if s[i] != '0' and s[i] != '1':
                    ch = s[i]
                    min_s = ''.join([ '0' if c == ch else c for c in s])
                    break
            else:
                min_s = ''.join(s)
        
        return int(max_s) - int(min_s)
