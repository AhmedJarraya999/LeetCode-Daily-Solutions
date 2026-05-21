class Solution:
    def minimumDeletions(self, s: str) -> int:
        n=len(s)
        a_count_right=[0]*(n+1)
        b_count_left=[0]*(n+1)
        for i in range(1,len(s)):
            if s[i-1]=="b":
                b_count_left[i]=b_count_left[i-1]+1
            else:
                b_count_left[i]=b_count_left[i-1]
        for i in range(len(s)-2,-1,-1):
            if s[i+1]=="a":
                a_count_right[i]=a_count_right[i+1]+1
            else:
                a_count_right[i]=a_count_right[i+1]
        res=len(s)
        for i in range(len(s)):
            deletions=a_count_right[i]+b_count_left[i]
            res=min(res,deletions)
        return res




# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         b_count = 0  # number of 'b' seen so far
#         res = 0  # minimum deletions
#         for c in s:O
#             if c == "b":
#                 b_count += 1
#             else:  # c == 'a'
#                 # either delete this 'a', or delete all previous 'b'
#                 res = min(res + 1, b_count)

        # return res
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         n = len(s)
        
#         # dp[i][0] = min deletions to make s[0..i] valid
#         #            and we are still in "a-phase" (no 'b' allowed yet)
#         #
#         # dp[i][1] = min deletions to make s[0..i] valid
#         #            and we are in "b-phase" (we allow b's after a's)
        
#         dp = [[0] * 2 for _ in range(n)]
        
#         # Base case for i = 0
#         if s[0] == 'a':
#             dp[0][0] = 0  # 'a' fits in a-phase
#             dp[0][1] = 0  # we can still decide to switch later
#         else:
#             dp[0][0] = 1  # must delete 'b' if staying in a-phase
#             dp[0][1] = 0  # no cost if we decide this is start of b-phase
        
#         # Build DP table
#         for i in range(1, n):
#             if s[i] == 'a':
                
#                 # Case 1: still in a-phase → 'a' is fine
#                 dp[i][0] = dp[i-1][0]
                
#                 # Case 2: in b-phase → 'a' is invalid, must delete it
#                 dp[i][1] = dp[i-1][1] + 1
                
#             else:  # s[i] == 'b'
                
#                 # Case 1: a-phase → 'b' is invalid, must delete it
#                 dp[i][0] = dp[i-1][0] + 1
                
#                 # Case 2: b-phase
#                 # either stay in b-phase or switch from a-phase
#                 dp[i][1] = min(
#                     dp[i-1][1],  # already in b-phase
#                     dp[i-1][0]   # switch from a-phase to b-phase
#                 )
        
#         # Final answer: best of both states
#         return min(dp[n-1][0], dp[n-1][1])






#         # n=len(s)
#         # prefix_b=[0]*(n+1)
#         # for i in range(len(s)):
#         #     prefix_b[i+1]=prefix_b[i]+(s[i]=='b')
#         # suffix_a = [0] * (n + 1)
#         # for i in range(n - 1, -1, -1):
#         #     suffix_a[i] = suffix_a[i + 1] + (s[i] == 'a')
#         # ans = float("inf")
#         # for i in range(n + 1):
#         #     deletions = prefix_b[i] + suffix_a[i]
#         #     ans = min(ans, deletions)
#         # return ans 


        # a_count_right=[0]*len(s)
        # for i in range(len(s)-2,-1,-1):
        #     if s[i]=="a":
        #         a_count_right[i]=a_count_right[i+1]+1
        #     else:
        #         a_count_right[i]=a_count_right[i+1]
        # b_count_left=0
        # res=float('inf')
        # for i in range(len(s)):
        #     deletions=b_count_left+a_count_right[i]
        #     res=min(res,deletions)
        #     if s[i]=="b":
        #         b_count_left+=1
        # return res