from collections import defaultdict

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # Helper to calculate partitions
        def count_partitions(s):
            partitions = 0
            i = 0
            while i < len(s):
                freq = defaultdict(int)
                j = i
                while j < len(s) and len(freq) <= k:
                    freq[s[j]] += 1
                    if len(freq) > k:
                        break
                    j += 1
                partitions += 1
                i = j
            return partitions
        
        # Case 1: No change
        max_parts = count_partitions(s)
        
        # Case 2: Try changing each character to any other letter
        for i in range(n):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if s[i] == c:
                    continue
                t = s[:i] + c + s[i+1:]
                max_parts = max(max_parts, count_partitions(t))
        
        return max_parts
