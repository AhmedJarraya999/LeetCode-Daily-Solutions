class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0

        # Find first non-'a' character
        while i < n and s[i] == 'a':
            i += 1

        # Perform the operation on the contiguous substring
        if i < n:
            while i < n and s[i] != 'a':
                s[i] = chr(ord(s[i]) - 1)
                i += 1
        else:
            # If all 'a's, decrement the last character
            s[-1] = 'z'

        return ''.join(s)