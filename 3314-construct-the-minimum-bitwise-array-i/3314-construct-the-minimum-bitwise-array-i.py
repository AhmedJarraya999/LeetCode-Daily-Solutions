class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        res = []

        for x in nums:
            curr = -1
            for c in range(x):
                if c | (c + 1) == x:
                    curr = c
                    break
            res.append(curr)

        return res
