# 
from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ###dp[i][state] heere
        #first did not work 
        # n = len(nums)
        # NEG = float('-inf')

        # # dp[i][state]
        # dp = [[NEG] * 3 for _ in range(n)]

        # # base case: start first element in increasing phase
        # dp[0][0] = nums[0]

        # for i in range(1, n):

        #     # 1️⃣ Increasing phase (state 0)
        #     if nums[i] > nums[i - 1]:
        #         dp[i][0] = max(
        #             dp[i - 1][0] + nums[i],  # continue increasing
        #             nums[i - 1] + nums[i]    # start new increasing segment
        #         )

        #     # 2️⃣ Decreasing phase (state 1)
        #     if nums[i] < nums[i - 1]:
        #         dp[i][1] = max(
        #             dp[i - 1][0] + nums[i],  # switch from increasing → decreasing
        #             dp[i - 1][1] + nums[i]   # continue decreasing
        #         )

        #     # 3️⃣ Second increasing phase (state 2)
        #     if nums[i] > nums[i - 1]:
        #         dp[i][2] = max(
        #             dp[i - 1][1] + nums[i],  # switch from decreasing → increasing
        #             dp[i - 1][2] + nums[i]   # continue second increasing
        #         )

        # return max(dp[i][2] for i in range(n))



###second



        n = len(nums)
        NEG = -10**18  # equivalent to Long.MIN_VALUE / 4

        inc1 = [NEG] * n
        dec = [NEG] * n
        inc2 = [NEG] * n

        for i in range(1, n):
            # First increasing phase
            if nums[i] > nums[i - 1]:
                inc1[i] = max(
                    inc1[i - 1] + nums[i],
                    nums[i - 1] + nums[i]
                )

            # Decreasing phase
            if nums[i] < nums[i - 1]:
                dec[i] = max(
                    inc1[i - 1] + nums[i],
                    dec[i - 1] + nums[i]
                )

            # Second increasing phase
            if nums[i] > nums[i - 1]:
                inc2[i] = max(
                    dec[i - 1] + nums[i],
                    inc2[i - 1] + nums[i]
                )

        return max(inc2)
       