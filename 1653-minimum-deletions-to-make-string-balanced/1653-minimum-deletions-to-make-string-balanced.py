class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0   # number of 'b' seen so far
        res = 0       # minimum deletions

        for c in s:
            if c == 'b':
                b_count += 1
            else:  # c == 'a'
                # either delete this 'a', or delete all previous 'b'
                res = min(res + 1, b_count)

        return res