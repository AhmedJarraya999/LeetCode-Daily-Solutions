class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        inc1 = [float("-inf")] * len(nums)
        dec = [float("-inf")] * len(nums)
        inc2 = [float("-inf")] * len(nums)
        for i in range(1, len(nums)):
            # max subarray sum ending at i foolow up order
            if nums[i] > nums[i - 1]:
                inc1[i] = max(nums[i] + inc1[i - 1], nums[i] + nums[i - 1])
            # max subarray sum ending at i foolow up  down order
            if nums[i] < nums[i - 1]:
                dec[i] = max(inc1[i - 1] + nums[i], dec[i - 1] + nums[i])
            # max subarray sum ending at i foolow up down up order
            if nums[i] > nums[i - 1]:
                inc2[i] = max(dec[i - 1] + nums[i], inc2[i - 1] + nums[i])
        return max(inc2)


### how to reduce this to one DP array with 3 states per index yes
# from typing import List

# class Solution:
#     def maxSumTrionic(self, nums: List[int]) -> int:
#         n = len(nums)
#         NEG = float('-inf')

#         dp = [[NEG]*3 for _ in range(n)]

#         dp[0][0] = nums[0]   # start increasing

#         for i in range(1, n):
#             # STATE 0: increasing
#             if nums[i] > nums[i-1]:
#                 dp[i][0] = max(
#                     nums[i],
#                     dp[i-1][0] + nums[i]
#                 )
#             else:
#                 dp[i][0] = nums[i]

#             # STATE 1: decreasing
#             if nums[i] < nums[i-1]:
#                 dp[i][1] = max(
#                     dp[i-1][0] + nums[i],
#                     dp[i-1][1] + nums[i]
#                 )

#             # STATE 2: increasing after decrease
#             if nums[i] > nums[i-1]:
#                 dp[i][2] = max(
#                     dp[i-1][1] + nums[i],
#                     dp[i-1][2] + nums[i]
#                 )

#         return max(dp[i][2] for i in range(n))
