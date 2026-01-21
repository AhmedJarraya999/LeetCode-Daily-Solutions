from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            res = -1
            pos = 0

            while (nums[i] & (1 << pos)) != 0:
                res = nums[i] ^ (1 << pos)
                pos += 1

            nums[i] = res

        return nums
