# 
from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
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