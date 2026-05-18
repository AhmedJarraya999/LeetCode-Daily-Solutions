class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0  # number of 'b' seen so far
        res = 0  # minimum deletions
        for c in s:
            if c == "b":
                b_count += 1
            else:  # c == 'a'
                # either delete this 'a', or delete all previous 'b'
                res = min(res + 1, b_count)

        return res
        # n=len(s)
        # prefix_b=[0]*(n+1)
        # for i in range(len(s)):
        #     prefix_b[i+1]=prefix_b[i]+(s[i]=='b')
        # suffix_a = [0] * (n + 1)
        # for i in range(n - 1, -1, -1):
        #     suffix_a[i] = suffix_a[i + 1] + (s[i] == 'a')
        # ans = float("inf")
        # for i in range(n + 1):
        #     deletions = prefix_b[i] + suffix_a[i]
        #     ans = min(ans, deletions)
        # return ans 

 
