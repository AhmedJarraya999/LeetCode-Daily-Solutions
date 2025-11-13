class Solution:
    def maxOperations(self, s: str) -> int:
        one_count = 0  # Count of '1's seen so far
        res = 0        # Total operations
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == "1":
                one_count += 1
            else:
                # Each '1' seen so far can move over this '0'
                res += one_count
                # Skip consecutive zeros (since each zero can be jumped by the same ones)
                while i + 1 < n and s[i + 1] == "0":
                    i += 1
            i += 1
        
        return res
