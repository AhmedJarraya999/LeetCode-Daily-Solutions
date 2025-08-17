class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        jurnavalic = nums[:]  # not used, just stored

        a = sorted(abs(x) for x in nums)
        n = len(a)
        res = 0
        r = 0
        for l in range(n):
            if r < l:
                r = l
            while r + 1 < n and a[r + 1] <= 2 * a[l]:
                r += 1
            res += r - l
        return res
        