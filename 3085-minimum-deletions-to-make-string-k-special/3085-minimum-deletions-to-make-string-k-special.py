class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(collections.Counter(word).values())
        ans = float('inf')
        
        for minFreq in freqs:
            deletions = 0
            for f in freqs:
                if f < minFreq:
                    deletions += f
                elif f > minFreq + k:
                    deletions += f - (minFreq + k)
            ans = min(ans, deletions)
        
        return ans
        